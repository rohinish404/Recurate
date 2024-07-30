# Recurate

A place to search over all your bookmarks or images saved on X (twitter).

Bookmarks is specific for me but this can also be used in a more generalised way... 

## How does it work?

<img width="673" alt="Screenshot 2024-07-30 at 10 02 23 PM" src="https://github.com/user-attachments/assets/92ddb08a-896f-451f-bb99-65b12a60dcb7">

## How to Use?

- Just go to any page on X (account, bookmarks, etc.) and use the scrape extension to scrape the tweets. Use [this](https://github.com/rohinish404/Recurate/blob/master/src/scrape/README.md) for setting up and using the extension.
- Clone the repository in your system.
```
git clone https://github.com/rohinish404/Recurate.git
cd Recurate
```
- Create a `data` folder inside `src` and paste both the files with names `bookmarks.json` and `image_data.json`.
- Create a venv for running the fastapi server as well as the scripts. (Advised to create in the root folder). Below are the commands for macos.
```
python3 -m venv venv
source venv/bin/activate
```
- Open the cloned repo in terminal and run the `execute.sh` file
```
./execute.sh
```
- Run the fastapi server. Port used in html scripts is 8000 so try to run the server on this port only.
```
fastapi run src/server/main.py
```
- Run the html scripts using serve command. (i use this command along with custom [live reload](https://github.com/rohinish404/Recurate/tree/master/src/live_reload) because i don't use vscode :"))
```
npm install -g serve
cd src
serve
```
- Use the app 🎉
  
**Note - Name the files as mentioned above only otherwise the app won't recognise these data files.**

## Demo


https://github.com/user-attachments/assets/3afc7466-2253-4b31-870e-6a925f5b47fa

## Further improvements (that can be made but i won't be working on it for sometime until i feel like :))


**Thanks for trying out. Do star⭐️ the repo if you found this useful**
