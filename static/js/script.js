(function(d, w) {
    w.addEventListener('resize', function() {
        const tabla = document.getElementById('tabla');
        // console.log(tabla);
        if (screen.width <= 800) {
            // console.log(tabla);
            // console.log('hola');
            tabla.classList.toggle('table-responsive')
            
        } else {
            console.log(tabla.classList);
        }
    })
})(document, window)