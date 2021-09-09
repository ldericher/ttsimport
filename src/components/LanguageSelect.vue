<template>
  <v-select
    label="Deck Language"
    prepend-icon="mdi-translate"
    :items="languages"
    dense
    filled
  />
</template>

<script>
export default {
  name: "LanguageSelect",

  data: () => ({
    languages: [
      { value: "en", text: "English" },
      { value: "fr", text: "French" },
      { value: "de", text: "German" },
      { value: "it", text: "Italian" },
      { value: "ja", text: "Japanese" },
      { value: "es", text: "Spanish" },
    ],
  }),
};
</script>
