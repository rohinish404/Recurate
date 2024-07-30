chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "TWEETS_EXTRACTED") {
    console.log(`Received ${message.tweets.length} tweets from the page`);
    chrome.runtime.sendMessage({type: "SAVE_TWEETS", tweets: message.tweets});
  }
});
