import { NestFactory } from '@nestjs/core';
import { LangchainModule } from './langchain/langchain.module';
import * as dotenv from 'dotenv';

async function bootstrap() {
  dotenv.config();
  const app = await NestFactory.create(LangchainModule);
  app.enableCors();
  await app.listen(3000);
  console.log('✅ LangChain service running on http://localhost:3000');
}
bootstrap();
