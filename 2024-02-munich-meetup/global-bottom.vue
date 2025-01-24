<template>
  <footer
    v-if="$nav.currentLayout !== 'cover'"
    class="absolute bottom-0 right-6 p-4"
  >
    {{ $nav.currentPage }}
  </footer>
</template>
