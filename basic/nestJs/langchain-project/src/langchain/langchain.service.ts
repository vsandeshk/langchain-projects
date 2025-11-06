import { Injectable } from '@nestjs/common';
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';
import { ChatPromptTemplate } from '@langchain/core/prompts';
import { StructuredOutputParser } from '@langchain/core/output_parsers';

@Injectable()
export class LangchainService {
    private readonly chat: ChatGoogleGenerativeAI;

    constructor() {
        const apiKey = process.env.GEMINI_API_KEY;
        if (!apiKey) {
            throw new Error('❌ Missing GEMINI_API_KEY in environment');
        }

        this.chat = new ChatGoogleGenerativeAI({
            model: 'gemini-2.5-flash',
            temperature: 0.0,
            apiKey,
        });

        console.log('✅ LangChain Gemini model initialized.');
    }

    /**
     * Normalize the model output to a string.
     */
    private extractText(content: any): string {
        if (typeof content === 'string') return content;
        if (Array.isArray(content)) {
            return content
                .map(item =>
                    typeof item === 'object' && 'text' in item ? (item as any).text : '',
                )
                .join(' ')
                .trim();
        }
        if (content && typeof content.text === 'string') {
            return content.text;
        }
        return '';
    }

    /**
     * Translate a text into a specific style using LangChain prompt templates.
     */
    async translateText(text: string, style: string): Promise<string> {
        const template = `
Translate the text delimited by triple backticks
into a style that is {style}.
text: \`\`\`{text}\`\`\`
`;
        const prompt = ChatPromptTemplate.fromTemplate(template);
        const messages = await prompt.formatMessages({ text, style });
        const response = await this.chat.invoke(messages);
        return this.extractText(response.content);
    }

    /**
     * Parse product review text into structured output.
     */
    async parseReview(reviewText: string): Promise<Record<string, any>> {
        // ✅ FIXED: use object map, not array
        const schemaDefinition = {
            gift: 'Was the item purchased as a gift? True/False.',
            delivery_days: 'Number of days for delivery, or -1 if unknown.',
            price_value: 'Sentences about value or price, as a list.',
        };

        const parser = StructuredOutputParser.fromNamesAndDescriptions(
            schemaDefinition,
        );
        const formatInstructions = parser.getFormatInstructions();

        const template = `
For the following text, extract:
- gift (True/False)
- delivery_days (number or -1)
- price_value (comma-separated sentences about price/value)

text: {text}

{format_instructions}
`;

        const prompt = ChatPromptTemplate.fromTemplate(template);
        const messages = await prompt.formatMessages({
            text: reviewText,
            format_instructions: formatInstructions,
        });

        const response = await this.chat.invoke(messages);
        const content = this.extractText(response.content);

        try {
            return await parser.parse(content);
        } catch (err) {
            console.warn('⚠️ Structured parsing failed:', err);
            return { raw: content };
        }
    }
}
