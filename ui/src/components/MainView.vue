<template>
  <v-main>
    <v-container>
      <v-img
        :src="require('../assets/yavook_big.png')"
        class="my-3 mx-auto"
        contain
        height="200"
      />

      <v-card flat class="mx-auto" max-width="1024">
        <v-card-text>
          <language-select v-model="language" />
          <decks-list v-model="deck_ids" />
        </v-card-text>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
import DecksList from "./DecksList.vue";
import LanguageSelect from "./LanguageSelect.vue";

export default {
  name: "MainView",

  components: {
    DecksList,
    LanguageSelect,
  },
};
</script>
