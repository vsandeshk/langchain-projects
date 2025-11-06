import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { LangchainService } from './langchain.service';
import { LangchainController } from './langchain.controller';

@Module({
    imports: [ConfigModule.forRoot()],
    providers: [LangchainService],
    controllers: [LangchainController],
})
export class LangchainModule { }
