<template>
  <v-card flat class="mx-auto" max-width="1024">
    <v-card-text>
      <decks-list v-model="deck_ids" />
      <language-select v-model="language" />
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="success"> Download Decks </v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
import DecksList from "./DecksList.vue";
import LanguageSelect from "./LanguageSelect.vue";

export default {
  name: "Decks",

  components: {
    DecksList,
    LanguageSelect,
  },

  data: () => ({
    language: "",
    deck_ids: ["6272690272862208"],
  }),
};
</script>