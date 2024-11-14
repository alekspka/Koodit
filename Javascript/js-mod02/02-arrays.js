
'use strict';

// taulukot eli arrays
const items = [1,2,3,4,5]
    console.log(items);

// alkioon viitataan ihan perus indeksillä

console.log(items[3])

// alkion arvoa voidaan muuttaa tai lisätä indeksin avulla

items[0] = 99;
console.log(items)
items[9] = 'Olen uusi jäsen';

// välissä on nyt ns määrittelemätön arvo/alkio eli undefined
console.log(items[6])

console.log('taulukon pituus:', items.length);

// taulukoiden läpikäynti loopin avulla

console.log('---------------------')
console.log('perinteinen for-i looppi')
for (let i = 0; i <items.length; i++){
    console.log(i,items[i]);
}

console.log('---------------------')
console.log('Läpikäynti for/in rakenteella, jolla saadaaan avain/indeksi ja arvo')
for (const index in items) {
    console.log(index, items[index]);
}
console.log('---------------------')
console.log('läpikäynti for/of rakenteella, jolla saadaan arvot')
for (const item of items) {
    // if lause jossa tutkitaan alkio undefined
if (item != undefined) {
    console.log(item);
}
}
console.log('---------------------')
console.log('---------------------')

    const names = ['Frank', 'Scott', 'Jasmine', 'Don']
    const ages = [18,21,22,110];

    for (let name of names) {
        console.log(`Name: ${name}`);
    }
// Järjestä aakkosjärjestykseen

names.sort();
    console.log(names);

names.reverse();
    console.log(names);

// ei toimi numeroiden kanssa sellaisenaan

ages.sort()
    console.log(ages);

// tämä toimii numeroiden kanssa

ages.sort((a,b) => a - b)
    console.log(ages);

ages.sort((a,b) => b - a)
    console.log(ages);

// lisätään nimi taulukkoon

names.push('Albert');
const newLength= names.push('Rita');
console.log(names);
console.log('Taulukon pituus', newLength);

// lisätään taulukon alkuun

names.unshift('Jooseppi');
console.log(names);

//poistetaan taulukon vika ja otetaan muuttuja talteen

const lastName = names.shift()
console.log('Poistettiin:',lastName)
console.log(names);

// etsitään onko taulukossa ko. arvo palauttaa true/false

console.log(names.includes('Scott'));

console.log('-----------------------');


// object literal eli olio
//samankaltainen kun pythonin sanakirja

const duck = {
    name: 'Aku Ankka',
    age: 313,
}
console.log(duck);
console.log(duck['age']);

// muutetaan arvoja

duck['age'] = 36;

duck.name = 'Hessu Hopo';

// lisätään uusia ominaisuuksia

duck.profession = 'im the plug';
console.log(duck);

// tietyn ominaisuuden arvon hakemineb

console.log(duck.name + ' on ' + duck.age, 'ikäinen ja motto: ' + duck.profession);

// metodin luominen olioon ns. nimettömänä funktiona

const duck2 = {
    name: 'Ines Ankka',
    age: 49,
    getInfo: function() {
        return this.name + ' on ' + this.age + '-vuotias.';
    }
}

console.log(duck2.getInfo());

console.log('---------------')

// preinteinen funktiomäärittely

function greet(name){
    console.log(`Greetings ${name}!`);
    return;
}

// function expression, funktio joka on anonyymi, mutta tallennetaan muuttujaan.

const greet2 = function(name)
{
    console.log(`Greetings again, ${name}!`);
}

const greet3 = (name) => {
    console.log(`Greetings a third time ${name}!`);
}

greet('Allu');
greet2('Allu');
greet3('Allu');

const nimi = 'Pena'
function logName(){
    console.log(nimi);
}
logName();