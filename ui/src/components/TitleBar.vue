<template>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title class="noselect">{{ page_title }}</v-toolbar-title>

    <v-spacer></v-spacer>

    <icon-text-button
      icon="mdi-github"
      text="View on Github"
      href="//github.com/ldericher/ttsimport"
    />
    <theme-toggle />
  </v-app-bar>
</template>

<script>
import IconTextButton from "./IconTextButton.vue";
import ThemeToggle from "./ThemeToggle.vue";
import VueConfig from "../../vue.config";

export default {
  name: "TitleBar",

  components: {
    IconTextButton,
    ThemeToggle,
  },

  computed: {
    page_title() {
      return VueConfig.pages.index.title;
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>