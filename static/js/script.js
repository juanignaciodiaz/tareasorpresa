(function(d, w) {
    w.addEventListener('resize', function() {
        const tabla = document.getElementById('tabla');
        // console.log(tabla);
        if (screen.width == 800 || screen.width == 360 || screen.width == 411 || screen.width == 320 || screen.width == 368) {
            // console.log(tabla);
            console.log(tabla.classList);
            for (const i in tabla.classList) {
                if (tabla.classList[i] == 'table-responsive') {
                    
                } else {
                    tabla.classList.toggle = 'table-responsive';
                }
            }
            // tabla.classList.toggle('table-responsive')
            
            
        } else if (screen.width > 800) {
            console.log('Soy mayor a 800');
            for (const i in tabla.classList) {
                if (tabla.classList[i] == 'table-responsive') {
                    tabla.classList.toggle = 'table-responsive';
                }
            }
        }
    })
})(document, window)