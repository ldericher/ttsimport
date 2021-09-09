<template>
  <v-btn :icon="sm_and_down" @click="toggle_mode" tabindex="-1" text>
    <v-icon
      >{{ dark_mode ? "mdi-weather-sunny" : "mdi-weather-night" }}
    </v-icon>
    <span class="hidden-sm-and-down ml-2">Toggle Theme</span>
  </v-btn>
</template>

<script>
export default {
  name: "ThemeToggle",

  computed: {
    dark_mode: {
      get() {
        return this.$vuetify.theme.dark;
      },
      set(mode) {
        this.$vuetify.theme.dark = mode;
      },
    },

    sm_and_down() {
      return this.$vuetify.breakpoint.smAndDown;
    },
  },

  methods: {
    toggle_mode() {
      this.dark_mode = !this.dark_mode;
    },
  },
};
</script>