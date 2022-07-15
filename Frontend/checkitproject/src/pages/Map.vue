<template>
    <div class="page">
        <button @click="MapCreate">create</button>
        <button @click="MapDestroy">destroy</button>
        <div id="map" class="map"></div>
    </div>
</template>

<script>
import $ from 'jquery'
export default{
data(){
    return{
        Map: undefined,
        StartPoint : undefined,
        places: [],
    }
    },
    mounted() {
            let recaptchaScript = document.createElement('script')
            recaptchaScript.setAttribute('src', 'https://mapgl.2gis.com/api/js/v1')
            document.head.appendChild(recaptchaScript)
        },
    methods:{
        MapCreate() {
            this.GetPlaces()
            console.log('Работает')
            this.Map = new mapgl.Map('map', {
                key: 'Your Api Key',
                center: [37.61811, 55.757523],
                zoom: 10,
            });
        },
        MapDestroy(){
            this.Map.destroy();
        },
        GetPlaces() {
            $.ajax({
                url: 'http://127.0.0.1:8000/coord/',
                type: 'GET',
                success: (response) => {
                    this.places = response
                    this.AddPlaces()
                },
                error: (data) => {
                    alert(data.responseJSON.non_field_errors[0])
                }
            })
        },
        AddPlaces(){
            const coords = new Array(this.places.length)
            for(let i = 0; i < this.places.length; i++){
                coords[i] = [this.places[i].cord_X, this.places[i].cord_Y]
            }
            coords.forEach((coord) => {
                const marker = new mapgl.Marker(this.Map, {
                    coordinates : coord,
                })
            })
        }
    }
    
}

</script>

<style scooped>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
.map{
    width: 100%;
    height: calc(100vh - 5rem);
}
</style>
