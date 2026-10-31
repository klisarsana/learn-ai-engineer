import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI();
  const MODEL = process.env.LLM_MODEL ?? "gemini-3.8-flash";

  const response = await ai.models.generateContent({
    model: MODEL,
    contents: "What is a neural network in one sentence?",
    config: {
      maxOutputTokens: 256,
    },
  });

  console.log(response.text);
}

main().catch(console.error);
