<template>
  <v-app-bar app color="primary" dark>
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
    <v-toolbar-title>{{ page_title }}</v-toolbar-title>

    <v-spacer></v-spacer>

    <theme-toggle />
  </v-app-bar>
</template>

<script>
import ThemeToggle from "./ThemeToggle.vue";
import VueConfig from "../../vue.config";

export default {
  name: "TitleBar",

  components: {
    ThemeToggle,
  },

  computed: {
    page_title: function () {
      return VueConfig.pages.index.title;
    },
  },
};
</script>