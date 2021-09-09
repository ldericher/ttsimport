<template>
  <v-card flat class="mx-auto" max-width="1024">
    <v-list flat>
      <v-list-item>
        <v-list-item-avatar>
          <v-icon>mdi-cards</v-icon>
        </v-list-item-avatar>
        <v-list-item-content> Deck ID here </v-list-item-content>
        <v-list-item-action>
          <v-btn color="error" icon>
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
      <v-list-item>
        <v-text-field
          label="Paste FF Decks Link or ID"
          placeholder="e.g. https://ffdecks.com/deck/6272690272862208"
        />
        <v-btn color="primary" text> Import </v-btn>
      </v-list-item>
    </v-list>
    <v-card-actions>
      <v-btn color="success mx-auto"> Download Decks </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "DecksList",

  data: () => ({
    deck_ids: [],
  }),
};
</script>