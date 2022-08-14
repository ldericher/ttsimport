<template>
  <v-list flat v-if="deck_ids.length > 0">
    <template v-for="(deck_id, idx) in deck_ids">
      <deck :key="idx" :deck_id="deck_id" :language="language" />

      <v-divider
        v-if="idx != deck_ids.length - 1"
        :key="idx + '_div'"
        class="my-2"
        role="presentation"
      />
    </template>
  </v-list>
</template>

<script>
import Deck from "./Deck.vue";

export default {
  name: "DecksList",

  components: {
    Deck,
  },

  props: {
    language: String,
  },

  data: () => ({
    deck_ids: ["1234", "5678"],
  }),

  methods: {
    add_deck(new_deck_id) {
      this.deck_ids.push(new_deck_id);
    },

    delete_deck(index) {
      if (index < this.deck_ids.length) {
        this.deck_ids.splice(index, 1);
      }
    },
  },
};
</script>
