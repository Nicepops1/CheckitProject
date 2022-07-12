const data = {
    Moskva: [
        {
        name: 'Москва',
        urlBackground: '../img/pic.jpg',
        description: 'Столица России'
        }
    ],
    SaintPetersburg: [{
        name: 'Санкт-Петербург',
        urlBackground: '../img/pic.jpg',
        description: 'Культурная столица России'
    }]
};
const element = document.getElementById('log-btn');


function townHandler(data){
    for(key in data){
        console.log(key + " " + data[key]);
    };
};
element.addEventListener( 'click', townHandler);