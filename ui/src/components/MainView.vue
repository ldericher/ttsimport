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
          <decks-list ref="list" :language="language" />
        </v-card-text>

        <v-divider />

        <v-card-actions>
          <deck-add-form @new="new_deck" />
        </v-card-actions>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
import DeckAddForm from "./DeckAddForm.vue";
import DecksList from "./DecksList.vue";
import LanguageSelect from "./LanguageSelect.vue";

export default {
  name: "MainView",

  components: {
    DecksList,
    LanguageSelect,
    DeckAddForm,
  },

  data: () => ({
    language: "",
  }),

  methods: {
    new_deck(new_deck_id) {
      this.$refs.list.add_deck(new_deck_id);
    },
  },
};
</script>
