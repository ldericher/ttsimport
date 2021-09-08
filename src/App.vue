<template>
  <v-app>
    <title-bar />

    <main-view />
  </v-app>
</template>

<script>
import TitleBar from "./components/TitleBar.vue";
import MainView from "./components/MainView.vue";

export default {
  name: "App",

  components: {
    TitleBar,
    MainView,
  },
};
</script>
