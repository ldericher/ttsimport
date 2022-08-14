<template>
  <v-list-item>
    <v-list-item-avatar>
      <v-icon color="primary">mdi-cards</v-icon>
    </v-list-item-avatar>

    <v-list-item-content class="noselect">
      <v-progress-linear v-if="loading" indeterminate />
      <template v-else> {{ deck_name }} ({{ card_count }} Cards) </template>
    </v-list-item-content>

    <v-list-item-icon>
      <v-tooltip v-if="!loading" left>
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

      <v-btn @click="delete_self" color="error" class="ml-2" icon outlined>
        <v-icon>mdi-delete</v-icon>
      </v-btn>

      <v-btn
        v-if="!loading"
        @click="download"
        color="success"
        class="ml-2"
        icon
        outlined
      >
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

  watch: {
    deck_id: {
      immediate: true,
      handler: "update_deckid",
    },
  },

  methods: {
    download() {},

    update_deckid(new_deck_id) {
      this.deck_name = null;

      this.$http({
        method: "POST",
        url: this.ttsimport_api_baseurl + "/ffdecks/summary",
        data: {
          language: this.$root.ttsimport_language,
          deck_id: new_deck_id,
        },
      })
        .then((response) => {
          this.deck_name = response.data.name;
          this.card_count = response.data.card_count;
        })
        .catch((error) => {
          console.error(error);
          this.delete_self();
        });
    },

    delete_self() {
      // index in parent vList
      this.$emit("delete");
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>