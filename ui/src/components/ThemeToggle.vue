<template>
  <icon-text-button
    :icon="dark_mode ? 'mdi-weather-sunny' : 'mdi-weather-night'"
    text="Toggle Theme"
    @click="toggle_mode"
  />
</template>

<script>
import IconTextButton from "./IconTextButton.vue";

export default {
  name: "ThemeToggle",

  components: {
    IconTextButton,
  },

  computed: {
    dark_mode: {
      get() {
        return this.$vuetify.theme.dark;
      },
      set(mode) {
        this.$vuetify.theme.dark = mode;
      },
    },
  },

  methods: {
    toggle_mode() {
      this.dark_mode = !this.dark_mode;
    },
  },
};
</script>