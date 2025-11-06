import { Body, Controller, Post } from '@nestjs/common';
import { LangchainService } from './langchain.service';

@Controller('langchain')
export class LangchainController {
    constructor(private readonly langchainService: LangchainService) { }

    /**
     * Translate text into a given style using Gemini LLM via LangChain.
     */
    @Post('translate')
    async translateText(
        @Body() body: { text: string; style: string },
    ): Promise<{ translated: string }> {
        const { text, style } = body;
        if (!text || !style) {
            throw new Error('❌ Both "text" and "style" are required.');
        }
        const translated = await this.langchainService.translateText(text, style);
        return { translated };
    }

    /**
     * Parse a product review into structured data using LangChain.
     */
    @Post('parse-review')
    async parseReview(
        @Body() body: { review: string },
    ): Promise<Record<string, any>> {
        const { review } = body;
        if (!review) {
            throw new Error('❌ "review" field is required.');
        }
        return await this.langchainService.parseReview(review);
    }
}
