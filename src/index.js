const all_tweets = document.getElementById("all_tweets")
const all_tweets2 = document.getElementById("all_tweets2")
const input_query = document.getElementById("myInput")
const input_query2 = document.getElementById("myInput2")
const search_btn = document.getElementById("search_btn")
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

      if (twt?.tweetContent.toUpperCase().indexOf(input_query.value?.toUpperCase()) > -1||twt?.username.toUpperCase().indexOf(input_query.value?.toUpperCase()) > -1) {
        console.log("hi")
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
  all_tweets2.innerHTML = '';

  fetch('http://localhost:8000/ask',{
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: input_query2.value }),
  })
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
        const tweetElement = document.createElement('div');
        tweetElement.id = "tweet2"
        tweetElement.innerHTML = `
<p>${item?.username}</p>
<p>${item?.tweetContent}</p>

`;
        all_tweets2.appendChild(tweetElement);
      });
    })
    .catch(error => console.error('Error:', error));



}

window.addEventListener('load', loadTweets);
input_query.addEventListener('input', loadTweets);
search_btn.addEventListener('click', semanticSearch);

