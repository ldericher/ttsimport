<template>
  <v-card flat class="mx-auto" max-width="1024">
    <v-card-text>
      <decks-list />
      <language-select />
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
};
</script>