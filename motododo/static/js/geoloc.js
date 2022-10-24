navigator.geolocation.getCurrentPosition(onSuccess, onError);

    function onSuccess(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        const coord = [lat, lon]
        coords = JSON.stringify(coord)
        document.getElementById("js_data_input").value = coords;

        let newInput = document.createElement('button');
        newInput.innerHTML = "Me Géolocaliser";
        newInput.classList.add("geoloc");
        let parentNode = document.getElementById('geolocform');
        parentNode.appendChild(newInput)
        
    }

    function onError(error) {
        console.log(error);
    }