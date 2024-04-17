apiKey="729cb1995dbc03b0634a9e6723f97806";
const apiurl="https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox= document.querySelector(".search input");
const searchbtn=document.querySelector(".search button");
async function checkweather(city){
    const response=await fetch(apiurl+city+`&appid=${apiKey}`);
    var data =await response.json();
    console.log(data);

    document.querySelector(".city").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = Math.round(data.main.temp)+ "°C";


}

searchbtn.addEventListener("click", ()=>{
    checkweather(searchBox.value);
})