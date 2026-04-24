<script setup lang="ts">
import { useAnalysisStore } from "@/stores/analysis";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { CheckCircle2, AlertCircle, Lightbulb } from "lucide-vue-next";
import { motion } from "motion-v";

const store = useAnalysisStore();

const variantClasses = {
  initial: { opacity: 0, y: 20, scale: 0.95 },
  animate: { opacity: 1, y: 0, scale: 1 },
  exit: { opacity: 0, y: 20, scale: 0.95 },
  transition: { type: "spring", stiffness: 300, damping: 20 } as const,
};
</script>

<template>
  <motion.div
    class="w-full max-w-3xl mx-auto mt-8 space-y-6 bg-background"
    :initial="variantClasses.initial"
    :animate="variantClasses.animate"
    :exit="variantClasses.exit"
    :transition="variantClasses.transition"
  >
    <Card
      :class="[
        'border-t-4',
        store.result!.score > 75 ? 'border-t-green-500' : 'border-t-yellow-500',
      ]"
    >
      <CardHeader class="pb-2">
        <CardTitle class="flex justify-between items-center text-xl">
          ATS Compatibility Score
          <span
            :class="[
              'text-4xl font-bold',
              store.result!.score > 75 ? 'text-green-600' : 'text-yellow-600',
            ]"
          >
            {{ store.result!.score }}%
          </span>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <p class="text-muted-foreground leading-relaxed">
          {{ store.result!.match_summary }}
        </p>
      </CardContent>
    </Card>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <Card>
        <CardHeader class="pb-2 flex flex-row items-center space-x-2">
          <AlertCircle class="w-5 h-5 text-destructive" />
          <CardTitle class="text-lg">Keyword Gaps</CardTitle>
        </CardHeader>
        <CardContent>
          <div
            v-if="store.result!.keyword_gaps.length > 0"
            class="flex flex-wrap gap-2"
          >
            <Badge
              v-for="gap in store.result!.keyword_gaps"
              :key="gap"
              variant="outline"
              class="bg-destructive/10 text-destructive border-destructive/20"
            >
              {{ gap }}
            </Badge>
          </div>
          <p v-else class="text-sm text-green-600 flex items-center">
            <CheckCircle2 class="w-4 h-4 mr-2" /> All essential keywords found!
          </p>
        </CardContent>
      </Card>

      <Card>
        <CardHeader class="pb-2 flex flex-row items-center space-x-2">
          <Lightbulb class="w-5 h-5 text-yellow-500" />
          <CardTitle class="text-lg">Improvement Tips</CardTitle>
        </CardHeader>
        <CardContent>
          <ul class="space-y-2">
            <li
              v-for="(tip, index) in store.result!.suggestions"
              :key="index"
              class="text-sm flex items-start"
            >
              <span class="mr-2 text-primary">•</span>
              {{ tip }}
            </li>
          </ul>
        </CardContent>
      </Card>
    </div>
  </motion.div>
</template>
