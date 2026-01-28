// Copyright (C) Microsoft Corporation.  
// Copyright (C) 2025 IAMAI CONSULTING CORP
//
// MIT License. All rights reserved.

using UnrealBuildTool;

public class Blocks : ModuleRules
{
	public Blocks(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = PCHUsageMode.NoSharedPCHs;
		PrivatePCHHeaderFile = "Blocks.h";
		bEnableExceptions = true;
		if (Target.Platform == UnrealTargetPlatform.Win64 && !Target.WindowsPlatform.Compiler.IsClang())
		{
			PrivateDefinitions.Add("__has_feature(x)=0");
		}

		PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore" });
	}
}
