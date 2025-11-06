import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { LangchainModule } from './langchain/langchain.module';

@Module({
  imports: [ConfigModule.forRoot(), LangchainModule],
})
export class AppModule { }
