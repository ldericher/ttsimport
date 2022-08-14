<template>
  <v-list-item>
    <v-list-item-avatar>
      <v-icon color="primary">mdi-cards</v-icon>
    </v-list-item-avatar>

    <v-list-item-content class="noselect">
      <v-progress-linear v-if="loading" indeterminate />
      <template v-else> {{ deck_name }} ({{ card_count }} Cards) </template>
    </v-list-item-content>

    <v-list-item-icon v-if="!loading">
      <v-tooltip left>
        <template v-slot:activator="{ on }">
          <v-btn
            v-if="card_count !== 50"
            v-on="on"
            color="warning"
            class="ml-2"
            icon
            outlined
          >
            <v-icon>mdi-flash-alert</v-icon>
          </v-btn>
        </template>
        Non-Standard deck size!
      </v-tooltip>

      <v-btn @click="$emit('delete')" color="error" class="ml-2" icon outlined>
        <v-icon>mdi-delete</v-icon>
      </v-btn>

      <v-btn @click="download" color="success" class="ml-2" icon outlined>
        <v-icon>mdi-download</v-icon>
      </v-btn>
    </v-list-item-icon>
  </v-list-item>
</template>

<script>
export default {
  name: "Deck",

  props: {
    deck_id: String,
  },

  computed: {
    loading() {
      return this.deck_name === null;
    },
  },

  data: () => ({
    deck_name: null,
    card_count: null,
  }),

  methods: {
    download() {
      console.log(this.$root.ttsimport_language);
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>