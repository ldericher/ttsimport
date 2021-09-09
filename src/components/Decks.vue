<template>
  <v-card flat class="mx-auto" max-width="1024">
    <v-card-text>
      <decks-list v-model="deck_ids" />
      <language-select v-model="language" />
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="download" color="success"> Download Decks </v-btn>
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
    language: null,
    deck_ids: null,
  }),

  methods: {
    download() {
      if (this.deck_ids.length > 0) {
        this.$http({
          url: "//" + window.location.hostname + ":5000/ffdecks/en", //" + this.language,
          method: "POST",
          responseType: "blob",
          data: { deck_ids: this.deck_ids },
        })
          .then((response) => {
            // save response
            let blob = new Blob([response.data], { type: "application/zip" });

            // redirect to browser
            let link = document.createElement("a");
            link.href = window.URL.createObjectURL(blob);
            link.download = "decks.zip";
            link.click();
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
  },
};
</script>