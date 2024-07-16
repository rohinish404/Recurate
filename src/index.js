//import tweet_data from "../data/tweet_data.json"
const all_tweets = document.getElementById("all_tweets")
const input_query = document.getElementById("myInput")

async function loadTweets(){
  try {
    const response = await fetch('../data/tweet_data.json');
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

window.addEventListener('load', loadTweets);
input_query.addEventListener('input', loadTweets);

