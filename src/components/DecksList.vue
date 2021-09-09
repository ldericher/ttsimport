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
            v-model="new_deck_id"
            :rules="new_deck_id_rules"
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

  props: {
    value: Array,
  },

  data: () => ({
    decks: [],
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

    this.$emit("input", this.current_deck_ids);
  },

  computed: {
    current_deck_ids() {
      var res = [];

      for (const deck of this.decks) {
        res.push(deck.id);
      }

      return res;
    },
  },

  methods: {
    import_deck() {
      if (this.valid && this.new_deck_id) {
        this.decks.push({ id: String(this.new_deck_id) });
        this.$refs.form.reset();

        this.$emit("input", this.current_deck_ids);
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
