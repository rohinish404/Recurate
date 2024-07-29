
const all_imgs = document.getElementById("all_imgs")
const search_btn = document.getElementById("search_img")
const Search_input = document.getElementById("search_input")

async function loadImages(){
  try {
    const response = await fetch('../data/image_links.json');
    const tweet_data = await response.json();
    all_imgs.innerHTML = '';
    tweet_data.forEach((item)=>{
        const tweetElement = document.createElement('div');
        tweetElement.className = "tweet_imgs"
        tweetElement.innerHTML = `
<img src="${item?.image_links}"></img> 

`;

      all_imgs.appendChild(tweetElement);

    })
  } catch (error) {
    console.error("error ", error)
  }
}

function fetchSearchResults() {
  all_imgs.innerHTML = ''
  fetch('http://localhost:8000/get_img_results',{ 
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query: Search_input.value }),
  })
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
        const tweetElement = document.createElement('div');
        tweetElement.className = "tweet_imgs"
        tweetElement.innerHTML = `
<img src="${item?.image_links}"></img> 

`;
        all_imgs.appendChild(tweetElement);
      });
    })
}
window.addEventListener('load',loadImages)
search_btn.addEventListener("click",fetchSearchResults)
