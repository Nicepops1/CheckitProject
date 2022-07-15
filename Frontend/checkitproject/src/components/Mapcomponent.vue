<template>
    <div id='map' class="map">
        
    </div>

</template>

<script>
export default{
    data(){

    },
    methods: {
        mounted() {
            const insertScript = document.createElement('script')
            insertScript.setAttribute('src', 'https://mapgl.2gis.com/api/js/v1')
            document.body.appendChild(insertScript)

            const map = new mapgl.Map('container', {
            key: 'Your API access key',
            center: [55.31878, 25.23584],
            zoom: 13,
        });
        },
    }
}</script>

<style scoped>
.map{
    width: 100%;
    height: 100vh;
}
</style>