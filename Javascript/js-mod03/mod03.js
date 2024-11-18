// Haetaan viittaus johonkin solmuun (node) DOMissa
const h1Elem = document.querySelector('h1')
console.log(h1Elem);

//muokataan DOMia
const title = h1Elem.textContent;
h1Elem.textContent = title + ' Lisäys Otsikkoon';
h1Elem.style.fontSize = '25px';
h1Elem.classList.add('text');

//piilotetaan elementti css:n avulla
h1Elem.classList.add('hidden');
//näytetään taas
h1Elem.classList.remove('hidden');

//ylemmän tason parent-elemtin piilotus
// h1Elem.parentElement.classList.add('hidden');

//lisätään sisältöä sivulle
const pElem = document.createElement('p')
document.querySelector('main').append(pElem)
pElem.textContent = 'Uusi Kappale by JS!';

// haetaan viittaus useampaan elementtiin/nodeen kerralla.
const paragraphs= document.querySelectorAll('p');
//console.log(paragraphs)
paragraphs[2].textContent = 'Kolmas kappale.';
//iteroidaan kaikki kappaleet läpi
// (const p of paragraphs){
 // p.textContent = 'Päivitetty!';
//}

// tehdään järjestetty listä jossa 5 alkiota
  const listContents = ['kynä','kumi','reppu','piano'];

// haetaan viittaus diviin id:n avulla
const listDiv = document.querySelector('#list');

function renderlist(items){
  listDiv.innerHTML = '';
const olElement = document.createElement('ol')
  for (let i= 0;i<items.length; i++){
      const newLi = document.createElement(('Li'))
      newLi.textContent = items[i];
      olElement.append(newLi);
    }
  listDiv.append(olElement)
  document.querySelector('main').append(olElement);
  document.querySelector()
}
//renderlist(listContents);
listContents.push('tietskari');
listContents.sort()
renderlist(listContents);

// BOM-rajapinta (window-olio)
// luetaan selaimen "sijainti" (URL)
window.console.log(window.location.href)
// siirrytään johonkin toiseen osoitteeseen
//window.location.href = 'https://www.google.fi';

//asioiden lisäys listalle
const addButton = document.querySelector('#add')
// asetetaan napille tapahtumankäsittelijä  click-eventille
addButton.addEventListener('click',()=>{
  const newItem = window.prompt("lisää jotakin listaan?");
  listContents.push(newItem);
  renderlist(listContents);
});