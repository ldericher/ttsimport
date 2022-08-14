<template>
  <v-container>
    <v-form ref="form" @submit.prevent="add_deck" v-model="valid">
      <v-row>
        <v-col cols="12" align="center" justify="center">
          <v-text-field
            placeholder="Paste FF Decks Link or ID here"
            hint="e.g. https://ffdecks.com/deck/6272690272862208 or 6272690272862208"
            v-model="deck_id"
            :rules="deck_id_rules"
            dense
            filled
          >
          </v-text-field>

          <v-btn color="error" @click="clear" tabindex="-1">
            <v-icon left>mdi-cancel</v-icon>
            Clear
          </v-btn>

          <v-btn color="success" type="submit" :disabled="!valid" class="ml-2">
            <v-icon left>mdi-plus</v-icon>
            Add Deck
          </v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: "DeckAddForm",

  data: () => ({
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
    clear() {
      this.$refs.form.reset();
    },

    add_deck() {
      if (this.deck_id && this.valid) {
        this.$emit("new", this.deck_id);
        this.$refs.form.reset();
      }
    },
  },
};
</script>

<style>
</style>