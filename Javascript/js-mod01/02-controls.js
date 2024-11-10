'use strict';
console.log('mro');

// arvotaan testinumero
const  randomNumber = Math.random()
console.log('arvottu numero',randomNumber)

// ehtolause, ehdon täytyy olla aina true/false
// 49,9% todennäköisyys kruuna/klaava
if (randomNumber<0.495) {
  console.log('kruuna')
}
else if (randomNumber>0.505){
  console.log('klaava')
}
else {
  console.log('kolikko jää kantilleen')
}

console.log('Suoritus jatkuu ehtolauseen jälkeen')