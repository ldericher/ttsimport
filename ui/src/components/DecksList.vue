<template>
  <v-list flat>
    <template v-for="(deck_id, idx) in deck_ids">
      <deck :key="idx" :deck_id="deck_id" />

      <v-divider
        v-if="idx != deck_ids.length - 1"
        :key="idx + '_div'"
        class="my-2"
        role="presentation"
      />
    </template>

    <v-form ref="form" @submit.prevent="add_deck" v-model="valid">
      <v-list-item>
        <v-list-item-content>
          <v-text-field
            placeholder="Paste FF Decks Link or ID here"
            hint="e.g. https://ffdecks.com/deck/6272690272862208 or 6272690272862208"
            v-model="new_deck_id"
            :rules="new_deck_id_rules"
            dense
            filled
          >
            <template v-slot:append-outer>
              <v-btn
                color="primary"
                type="submit"
                :disabled="!valid"
                icon
                outlined
              >
                <v-icon>mdi-check</v-icon>
              </v-btn>
            </template>
          </v-text-field>
        </v-list-item-content>
      </v-list-item>
    </v-form>
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
    value: Array,
  },

  data: () => ({
    deck_ids: ["1234", "5678"],
    valid: false,
    new_deck_id: "",
    new_deck_id_rules: [
      (v) =>
        !v ||
        /^((https?:\/\/)?ffdecks\.com(\/+api)?\/+deck\/+)?([0-9]+)/.test(v) ||
        "Deck ID is malformed",
    ],
  }),

  mounted() {
    if (Array.isArray(this.value)) {
      for (const deck_id of this.value) {
        this.decks.push({ id: String(deck_id) });
      }
    }

    this.$emit("input", this.deck_ids);
  },

  methods: {
    add_deck() {
      if (this.new_deck_id && this.valid) {
        const new_deck_id = this.new_deck_id;
        this.$refs.form.reset();

        this.deck_ids.push(new_deck_id);
      }
    },

    delete_deck(index) {
      if (index < this.decks.length) {
        this.decks.splice(index, 1);

        this.$emit("input", this.current_deck_ids);
      }
    },
  },
};
</script>

<style scoped>
.noselect {
  user-select: none;
}
</style>
