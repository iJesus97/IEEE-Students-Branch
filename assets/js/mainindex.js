new Vue({
  el: "#transition-components-demo",
  data: {
    view: "v-a",
  },
  components: {
    "v-a": {
      template: "<div><h1>Eius dolores natus tenetur nobis.</h1><p>Architecto sed non possimus. Corporis quia omnis eius architecto voluptas deserunt rerum optio id. Voluptates ipsa ducimus doloribus repellendus optio aut ullam reiciendis.</p><a href=\"en/\">Ir a la página principal</a></div>",
    },
    "v-b": {
      template: "<div><h1>Bienvenido a la página oficial de la rama IEEE del TecNM Atlixco</h1><p>En este sitio podrás encontrar las noticias, eventos y la tienda de la rama IEEE</p><a href=\"es/\">Ir a la página principal</a></div>",
    },
  },
});
