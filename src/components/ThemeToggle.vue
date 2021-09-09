<template>
  <v-btn @click="toggle_mode" text :icon="sm_and_down">
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
      get: function () {
        return this.$vuetify.theme.dark;
      },
      set: function (mode) {
        this.$vuetify.theme.dark = mode;
      },
    },

    sm_and_down: function () {
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