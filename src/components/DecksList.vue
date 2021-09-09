<template>
  <v-list flat>
    <template v-for="(deck, idx) in decks">
      <v-list-item :key="idx">
        <v-list-item-avatar>
          <v-icon color="primary">mdi-cards</v-icon>
        </v-list-item-avatar>

        <v-list-item-content> {{ deck.id }} </v-list-item-content>

        <v-list-item-action>
          <v-btn
            @click="delete_deck(idx)"
            color="error"
            tabindex="-1"
            icon
            outlined
          >
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>

      <v-divider
        v-if="idx != decks.length - 1"
        :key="idx + '_div'"
        class="my-2"
        role="presentation"
      />
    </template>

    <v-form ref="form" @submit.prevent="import_deck" v-model="valid">
      <v-list-item>
        <v-list-item-content>
          <v-text-field
            placeholder="Paste FF Decks Link or ID"
            hint="e.g. https://ffdecks.com/deck/6272690272862208 or 6272690272862208"
            v-model="deck_id"
            :rules="deck_id_rules"
            dense
            filled
          >
            <template v-slot:append-outer>
              <v-btn color="primary" type="submit" :disabled="!valid" text>
                Import
              </v-btn>
            </template>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </v-form>
  </v-list>
</template>

<script>
export default {
  name: "DecksList",

  data: () => ({
    decks: [{ id: 6272690272862208 }],
    valid: false,
    deck_id: "",
    deck_id_rules: [
      (v) =>
        !v ||
        /^((https?:\/\/)?ffdecks\.com(\/+api)?\/+deck\/+)?([0-9]+)/.test(v) ||
        "Deck ID is malformed",
    ],
  }),

  methods: {
    import_deck() {
      if (this.valid && this.deck_id) {
        this.decks.push({ id: this.deck_id });
        this.$refs.form.reset();
      }
    },

    delete_deck(index) {
      if (index < this.decks.length) {
        this.decks.splice(index, 1);
      }
    },
  },
};
</script>
