<template>
  <v-list flat v-if="deck_ids.length > 0">
    <template v-for="(deck_id, index) in deck_ids">
      <deck :key="index" :deck_id="deck_id" @delete="delete_deck(index)" />

      <v-divider
        v-if="index != deck_ids.length - 1"
        :key="index + '_div'"
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

  data: () => ({
    deck_ids: [],
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
