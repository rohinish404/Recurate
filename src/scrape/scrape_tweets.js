function extractTweetData(tweet) {
  const usernameElement = tweet.querySelector('div[data-testid="User-Name"] span');
  const username = usernameElement ? usernameElement.textContent : 'Unknown';

  const tweetTextElement = tweet.querySelector('div[data-testid="tweetText"]');
  const tweetContent = tweetTextElement ? tweetTextElement.textContent : '';

  const mediaElements = tweet.querySelectorAll('div[data-testid="tweetPhoto"], div[data-testid="videoPlayer"]');
  const media = Array.from(mediaElements).map(el => {
    if (el.dataset.testid === 'tweetPhoto') {
      return el.querySelector('img')?.src;
    } else {
      return el.querySelector('video')?.src;
    }
  });

  const timestampElement = tweet.querySelector('a time');
  const tweetLink = timestampElement ? timestampElement.parentElement.href : '';

  return { username, tweetContent, media, tweetLink };
}

async function scrollAndExtract(maxScrolls = 100) {
  let scrollCount = 0;
  let lastHeight = document.documentElement.scrollHeight;
  const uniqueTweets = new Map();

  while (scrollCount < maxScrolls) {
    const tweets = document.querySelectorAll('article[data-testid="tweet"]');
    console.log(`Found ${tweets.length} tweets on the page`);

    tweets.forEach(tweet => {
      const tweetData = extractTweetData(tweet);
      if (tweetData.tweetLink && !uniqueTweets.has(tweetData.tweetLink)) {
        uniqueTweets.set(tweetData.tweetLink, tweetData);
      }
    });

    console.log(`Total unique tweets collected: ${uniqueTweets.size}`);

    window.scrollBy(0, 5000);
    await new Promise(resolve => setTimeout(resolve, 3000));

    const currentHeight = document.documentElement.scrollHeight;
    if (currentHeight === lastHeight) {
      console.log("Height hasn't changed. Ending scroll.");
      break;
    }
    lastHeight = currentHeight;

    scrollCount++;
    console.log(`Scroll ${scrollCount} completed`);
  }

  return Array.from(uniqueTweets.values());
}

async function scrollExtractAndSave() {
  console.log("Starting to scroll and extract tweets");
  const tweets = await scrollAndExtract();

  console.log(`Preparing to save ${tweets.length} unique tweets to JSON`);
  const jsonData = JSON.stringify(tweets, null, 2);
  const blob = new Blob([jsonData], {type: 'application/json'});
  const url = URL.createObjectURL(blob);

  const a = document.createElement('a');
  a.href = url;
  a.download = 'tweet_data.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);

  console.log(`Extracted and saved ${tweets.length} unique tweets.`);
}

scrollExtractAndSave();
