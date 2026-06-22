let productos = JSON.parse(localStorage.getItem("productos")) || [];


mostrarProductos();



// =====================
// AGREGAR PRODUCTO
// =====================


function agregarProducto(){


let idProducto = productos.length + 1;



let producto = {


idProducto:idProducto,


nombreProducto:
document.getElementById("nombre").value,


categoria:
document.getElementById("categoria").value,


tipoMascota:
document.getElementById("mascota").value,


edad:
document.getElementById("edad").value,


descripcion:
document.getElementById("descripcion").value,


personalizable:
document.getElementById("personalizable").checked,


precio:
Number(document.getElementById("precio").value),


stock:
Number(document.getElementById("stock").value),


proveedor:
document.getElementById("proveedor").value



};



productos.push(producto);



guardarProductos();



mostrarProductos();



limpiarFormulario();



alert(
"Producto agregado. ID: " + idProducto
);


}




// =====================
// GUARDAR
// =====================


function guardarProductos(){


localStorage.setItem(

"productos",

JSON.stringify(productos)

);


}





// =====================
// MOSTRAR
// =====================


function mostrarProductos(){


let lista =
document.getElementById("listaProductos");



lista.innerHTML="";



productos.forEach(p=>{


lista.innerHTML += `


<div class="producto">


<h3>

${p.nombreProducto}

</h3>


<p>ID: ${p.idProducto}</p>

<p>Categoría: ${p.categoria}</p>

<p>Mascota: ${p.tipoMascota}</p>

<p>Edad: ${p.edad}</p>

<p>Precio: $${p.precio}</p>

<p>Stock: ${p.stock}</p>


</div>



`;


});

}




// =====================
// BUSCAR
// =====================


function buscarProducto(){



let id =
Number(document.getElementById("buscarID").value);



let resultado =
document.getElementById("resultadoBusqueda");



let producto =
productos.find(
p=>p.idProducto===id
);



if(producto){


resultado.innerHTML=`


<div class="producto">


<h3>
${producto.nombreProducto}
</h3>


<p>Categoría: ${producto.categoria}</p>

<p>Mascota: ${producto.tipoMascota}</p>

<p>Edad: ${producto.edad}</p>

<p>Precio: $${producto.precio}</p>



</div>



`;



}else{


resultado.innerHTML=
"Producto no encontrado";


}


}





// =====================
// BORRAR TODO
// =====================


function borrarProductos(){



let confirmar =
confirm(
"¿Seguro que querés eliminar todos los productos?"
);



if(confirmar){


productos=[];


localStorage.removeItem("productos");



mostrarProductos();



alert(
"Todos los productos fueron eliminados"
);


}



}





// =====================
// LIMPIAR FORMULARIO
// =====================


function limpiarFormulario(){


document.getElementById("nombre").value="";

document.getElementById("descripcion").value="";

document.getElementById("precio").value="";

document.getElementById("stock").value="";

document.getElementById("proveedor").value="";

document.getElementById("personalizable").checked=false;


}