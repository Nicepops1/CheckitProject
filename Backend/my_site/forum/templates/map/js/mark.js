const map = new mapgl.Map('container', {
    center: [37.64, 55.76],
    zoom: 8,
    key: '123',
    style: 'c080bb6a-8134-4993-93a1-5b4d8c36a59b'
});
const marker = new mapgl.Marker(map, {
    coordinates: [38.64, 55.76],
    icon: 'https://docs.2gis.com/img/mapgl/marker.svg',
});
const tooltipEl = document.getElementById('tooltip');
marker.on('mouseover', (event) => {
    // Offset in pixels
    const offset = 5;
    tooltipEl.style.top = `${event.point[1] + offset}px`;
    tooltipEl.style.left = `${event.point[0] + offset}px`;
    tooltipEl.style.display = 'block';
});
marker.on('mouseout', (e) => {
    tooltipEl.style.display = 'none';
});