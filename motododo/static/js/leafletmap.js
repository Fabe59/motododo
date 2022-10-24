// Création d'une liste vide pour les coordonnées et le centrage de la carte
bounds = []

// Création de la map
let map = L.map('mapid');

// Création et ajout du tyleLayer à la map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 17,
}).addTo(map);

// Création des marqueurs
let result_elt = document.querySelectorAll('.result_elt');
for (var i = 0; i < result_elt.length; i++) {
    let lat = (result_elt[i].querySelector('.lat').textContent).replace(",", ".")
    let lon = (result_elt[i].querySelector('.lon').textContent).replace(",", ".")
    let name = result_elt[i].querySelector('.name').textContent
    let coord = [lat, lon]
    bounds.push(coord)
    let popup = L.popup({
        closeButton: false,
        closeOnEscapeKey: false,
        closeOnClick: false,
        autoClose: false,
    })
    .setLatLng(coord)
    .setContent(name)
    .addTo(map)
    result_elt[i].addEventListener('mouseover', function() {
        popup.getElement().classList.add('is-active')
    })
    result_elt[i].addEventListener('mouseleave', function() {
        popup.getElement().classList.remove('is-active')
    })
  };

// Centrage dynamique de la carte
if (bounds.length >= 2) {
    map.fitBounds(bounds);
}
else {
    map.setView([result_elt[0].querySelector('.lat').textContent.replace(",", "."), result_elt[0].querySelector('.lon').textContent.replace(",", ".")], 15);
};

