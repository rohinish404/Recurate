const all_tweets = document.getElementById("all_tweets")
const input_query = document.getElementById("myInput")
const search_btn = document.getElementById("search_btn")
const toggleCheck = document.getElementById("toggleCheck")

async function loadTweets(){
  try {
    const response = await fetch('../data/bookmarks.json');
    const tweet_data = await response.json();
    all_tweets.innerHTML = '';
    tweet_data.forEach((twt)=>{
      const tweetElement = document.createElement('div');
      tweetElement.id = "tweet"
      tweetElement.innerHTML = `
<p>${twt?.username}</p>
<p>${twt?.tweetContent}</p>
<img src="${twt?.media[0]}"></img> 
`;

      if (twt?.tweetContent.toUpperCase().includes(input_query.value?.toUpperCase()) ||twt?.username.toUpperCase().includes(input_query.value?.toUpperCase())) {
        tweetElement.style.display = "";
      } else {
        tweetElement.style.display = "none";
      }


      all_tweets.appendChild(tweetElement);

    })
  } catch (error) {
    console.error("error ", error)
  }
}

function semanticSearch() {
  all_tweets.innerHTML = '';
  fetch('http://localhost:8000/ask',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: input_query.value }),
  })
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
        const tweetElement = document.createElement('div');
        tweetElement.id = "tweet"
        tweetElement.innerHTML = `
<p>${item?.username}</p>
<p>${item?.tweetContent}</p>

`;
        all_tweets.appendChild(tweetElement);
      });
    })
    .catch(error => console.error('Error:', error));
}

function handleSearch() {
  if (toggleCheck.checked) {
    console.log("Calling semanticSearch");
    semanticSearch();
  } else {
    console.log("Calling loadTweets");
    loadTweets();
  }
}
window.addEventListener('load', () => {
  loadTweets();
  input_query.addEventListener('input', handleSearch);
});
