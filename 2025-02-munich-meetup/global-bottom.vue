<template>
  <footer
    v-if="$nav.currentLayout !== 'cover'"
    class="absolute bottom-0 right-4 p-4"
  >
    {{ $nav.currentPage }}
  </footer>
</template>
