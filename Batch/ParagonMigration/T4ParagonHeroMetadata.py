# Copyright VirtualFlow, Inc. All Rights Reserved.
import unreal
import sys

GContentName = None
GSourcePath = None
GOutputPath = None
GHeroObject = None

def init_stance(stance):
    GHeroObject.set_stance_name(stance)
    return

def add_state_idle(a):
    GHeroObject.add_state_layer_anim_sequence("Idle", a)
    return

def add_state_aim(a):
    GHeroObject.add_state_layer_blend_space("Aim", a)
    return

def add_state_fwdrun(Loop, Start, End):
    GHeroObject.add_state_layer_blend_space("FwdRun", Loop)
    GHeroObject.add_state_layer_anim_sequence("FwdRunStart", Start)
    GHeroObject.add_state_layer_anim_sequence("FwdRunStop", End)
    return

def add_state_bwdrun(Loop, Start, End):
    GHeroObject.add_state_layer_blend_space("BwdRun", Loop)
    GHeroObject.add_state_layer_anim_sequence("BwdRunStart", Start)
    GHeroObject.add_state_layer_anim_sequence("BwdRunStop", End)
    return

def add_state_leftrun(Loop, Start, End):
    GHeroObject.add_state_layer_blend_space("LeftRun", Loop)
    GHeroObject.add_state_layer_anim_sequence("LeftRunStart", Start)
    GHeroObject.add_state_layer_anim_sequence("LeftRunStop", End)
    return

def add_state_rightrun(Loop, Start, End):
    GHeroObject.add_state_layer_blend_space("RightRun", Loop)
    GHeroObject.add_state_layer_anim_sequence("RightRunStart", Start)
    GHeroObject.add_state_layer_anim_sequence("RightRunStop", End)
    return

def add_system_turn(l90, l180, r90, r180):
    GHeroObject.add_system_layer_anim_sequence("TurnLeft90", l90, False)
    GHeroObject.add_system_layer_anim_sequence("TurnLeft180", l180, False)
    GHeroObject.add_system_layer_anim_sequence("TurnRight90", r90, False)
    GHeroObject.add_system_layer_anim_sequence("TurnRight180", r180, False)
    return

def add_system_hit(front, back, left, right):
    GHeroObject.add_system_layer_anim_sequence("HitReactFront", front, False)
    GHeroObject.add_system_layer_anim_sequence("HitReactBack", back, False)
    GHeroObject.add_system_layer_anim_sequence("HitReactLeft", left, False)
    GHeroObject.add_system_layer_anim_sequence("HitReactRight", right, False)
    return

def add_system_bound(bound):
    GHeroObject.add_system_layer_anim_sequence("Bound", bound, False)
    return

def add_system_stun(start, loop, end):
    GHeroObject.add_system_layer_anim_sequence("StunStart", start, False)
    GHeroObject.add_system_layer_anim_sequence("StunLoop", loop, False)
    GHeroObject.add_system_layer_anim_sequence("StunEnd", end, False)
    return

def add_system_knockback(front, back, up):
    GHeroObject.add_system_layer_anim_sequence("KnockbackFrontLoop", front, False)
    GHeroObject.add_system_layer_anim_sequence("KnockbackBackLoop", back, False)
    GHeroObject.add_system_layer_anim_sequence("KnockbackBackUp", up, False)
    return

def add_system_jump(start, loop, fall, land, recovery):
    GHeroObject.add_system_layer_anim_sequence("JumpStart", start, False)
    GHeroObject.add_system_layer_anim_sequence("JumpLoop", loop, False)
    GHeroObject.add_system_layer_anim_sequence("JumpFall", fall, False)
    GHeroObject.add_system_layer_anim_sequence("JumpLand", land, False)
    GHeroObject.add_system_layer_anim_sequence("JumpRecovery", recovery, False)
    return

def add_system_death(a, b):
    GHeroObject.add_system_layer_anim_sequence("DeathA", a, True)
    GHeroObject.add_system_layer_anim_sequence("DeathB", b, True)
    return

def add_system_resurrect(a):
    GHeroObject.add_system_layer_anim_sequence("Resurrect", a, False)
    return

##
# Crunch
##
def Init_Crunch(target_heros):
    HeroName = "Crunch"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = True


    # GameData
    GHeroObject.game_data_info.race_name = "WhiteHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.SWING
    
    GHeroObject.game_data_info.bound_height = 250
    GHeroObject.game_data_info.bound_radius = 100
    
    GHeroObject.game_data_info.default_move_speed = 300
    GHeroObject.game_data_info.combat_move_speed = 250
    GHeroObject.game_data_info.sprint_move_speed = 600
    
    GHeroObject.game_data_info.weapon_name = "Punch"
    
    GHeroObject.game_data_info.jump_max_height = 150
    GHeroObject.game_data_info.jump_height_speed = 100
    
    GHeroObject.game_data_info.sensory_range = 3000
    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 190
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle_Combat")
    add_state_aim("Crunch_AO_Blendspace")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death_A", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Jump_Start", "LaunchPad", "None", "Jump_PreLand", "Jump_Land")
    add_system_knockback("Knockback_Front", "Knockback_Back", "None")
    add_system_stun("Stunned_Start", "Stunned_Loop", "None")
    add_system_turn("Idle_90_Turn_Left", "Idle_180_Turn_Left", "Idle_90_Turn_Right", "Idle_180_Turn_Right")
    add_system_bound("Bound")
    add_system_resurrect("None")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 300, 25, 200)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 300, 300)

    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.23, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Ability_Combo_01")
    GHeroObject.add_animation_action("Attack_A_Recovery", "Ability_Combo_01_Recovery")
    GHeroObject.add_particle_action("Attack_A", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_l", 0.23, 0.0, 1.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.23, 0.0)
    GHeroObject.add_animation_action("Attack_B", "Ability_Combo_02")
    GHeroObject.add_animation_action("Attack_B_Recovery", "Ability_Combo_02_Recovery")
    GHeroObject.add_particle_action("Attack_B", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_r", 0.2, 0.0, 1.0)

    # Skill layer : Attack_C
    GHeroObject.add_skill_property("Attack_C", "T4HeroNormalSkillStat", "Hit", 0.23, 0.0)
    GHeroObject.add_animation_action("Attack_C", "Ability_Combo_03")
    GHeroObject.add_particle_action("Attack_C", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_l", 0.23, 0.0, 1.0)

    # Skill layer : Attack_D
    GHeroObject.add_skill_property("Attack_D", "T4HeroNormalSkillStat", "Hit", 0.2, 0.0)
    GHeroObject.add_animation_action("Attack_D", "Ability_Combo_04")
    GHeroObject.add_particle_action("Attack_D", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_r", 0.2, 0.0, 1.0)

    # Skill layer : Attack_E
    GHeroObject.add_skill_property("Attack_E", "T4HeroCriticalSkillStat", "Hit", 0.4, 50.0)
    GHeroObject.add_animation_action("Attack_E", "Ability_Hook")
    GHeroObject.add_particle_action("Attack_E", "P_Crunch_Hook_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_l", 0.4, 0.0, 1.0)

    # Skill layer : Attack_F
    GHeroObject.add_skill_property("Attack_F", "T4HeroCriticalSkillStat", "Hit", 0.25, 50.0)
    GHeroObject.add_animation_action("Attack_F", "Ability_Uppercut")
    GHeroObject.add_particle_action("Attack_F", "P_Crunch_Uppercut_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_r", 0.25, 0.0, 1.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.25, 500.0)
    GHeroObject.add_animation_action("Skill_Q", "Ability_Attack_Air")
    GHeroObject.add_particle_action("Skill_Q", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_r", 0.25, 0.0, 1.0)
    GHeroObject.add_movement_action("Skill_Q", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.FRONT, 500, 250.0, 300)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.43, 200.0)
    GHeroObject.add_animation_action("Skill_E", "Ability_DashingCross")
    GHeroObject.add_animation_action("Skill_E_Recovery", "Ability_Dashing_Recovery")
    GHeroObject.add_particle_action("Skill_E", "P_Crunch_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_l", 0.43, 0.0, 1.0)
    GHeroObject.add_movement_action("Skill_E", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.FRONT, 200, 50.0, 50)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "Level_Start");
    GHeroObject.add_animation_action("SelectStart", "LevelStart_Alt");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_Laugh");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_King");


    # Sprint stance
    init_stance("Sprint")

    add_state_idle("Idle_TravelMode")
    add_state_aim("Crunch_AO_Blendspace")

    return


##
# Sparrow
##
def Init_Sparrow(target_heros):
    HeroName = "Sparrow"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = True


    # GameData
    GHeroObject.game_data_info.race_name = "DarkHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.THROW
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 50
    
    GHeroObject.game_data_info.default_move_speed = 500
    GHeroObject.game_data_info.combat_move_speed = 400
    GHeroObject.game_data_info.sprint_move_speed = 800
    
    GHeroObject.game_data_info.weapon_name = "Bow"
    
    GHeroObject.game_data_info.jump_max_height = 250
    GHeroObject.game_data_info.jump_height_speed = 200
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 1200
    

    # defualt stance
    init_stance("Default")

    add_state_idle("idle")
    add_state_aim("AO_idle")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRgtSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death_Fwd", "Death_Bwd")
    add_system_hit("HitReact_Fwd", "HitReact_Bwd", "HitReact_Left", "Hitreact_Right")
    add_system_jump("Jump_Start", "JumpPad", "None", "Jump_Land", "Jump_Recovery")
    add_system_knockback("Knock_Bwd", "Knock_Fwd", "Knock_Up")
    add_system_stun("Stunned_Start", "Stunned_Loop", "None")
    add_system_turn("Turn_Left_90", "Turn_Left_180", "Turn_Right_90", "Turn_Right_180")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 500, 100, 500)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 500, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Primary_Fire_Med")
    GHeroObject.add_particle_action("Attack_A", "P_Sparrow_PrimaryAttack", unreal.T4AttachParent.DEFAULT, "arrow_anchor", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Attack_A", "P_SparrowPrimaryMuzzleFlash", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_A", "P_Sparrow_PrimaryAttack", "P_Sparrow_Primary_Ballistic_HitPlayer", "arrow_anchor", unreal.T4MovementType.PARABOLA, 1300, 50.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Attack_B", "R_Ability_Med_Fire")
    GHeroObject.add_particle_action("Attack_B", "P_Sparrow_PrimaryAttack", unreal.T4AttachParent.DEFAULT, "arrow_anchor", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Attack_B", "P_SparrowPrimaryMuzzleFlash", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_B", "P_Sparrow_PrimaryAttack", "P_Sparrow_Primary_Ballistic_HitPlayer", "arrow_anchor", unreal.T4MovementType.PARABOLA, 1300, 50.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.2, 0.0)
    GHeroObject.add_animation_action("Skill_Q", "Q_Ability")
    GHeroObject.add_particle_action("Skill_Q", "P_Sparrow_PrimaryAttack", unreal.T4AttachParent.DEFAULT, "arrow_anchor", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_SparrowPrimaryMuzzleFlash", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.2, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Sparrow_Burst", unreal.T4AttachParent.DEFAULT, "Root", 0.2, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_Q", "P_Arrow_Ultimate", "P_Sparrow_UltHit", "arrow_anchor", unreal.T4MovementType.PARABOLA, 1000, 300.0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "LevelStart_Alt");
    GHeroObject.add_animation_action("SelectStart", "Emote_Handstand_T3");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_Bow_M1");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_Taunt_KickUpDust_M2");


    # Sprint stance
    init_stance("Sprint")

    add_state_idle("Travel_mode_Idle")
    add_state_aim("AO_TravelMode")
    add_state_fwdrun("SprintFwdSlopeLean", "Sprint_Fwd_Start", "Sprint_Fwd_Stop")
    add_state_bwdrun("SprintBwdSlopeLean", "Sprint_Bwd_Start", "Sprint_Bwd_Stop")

    return


##
# Terra
##
def Init_Terra(target_heros):
    HeroName = "Terra"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = False


    # GameData
    GHeroObject.game_data_info.race_name = "WhiteHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.SWING
    
    GHeroObject.game_data_info.bound_height = 250
    GHeroObject.game_data_info.bound_radius = 80
    
    GHeroObject.game_data_info.default_move_speed = 350
    GHeroObject.game_data_info.combat_move_speed = 300
    GHeroObject.game_data_info.sprint_move_speed = 700
    
    GHeroObject.game_data_info.weapon_name = "Axe"
    
    GHeroObject.game_data_info.jump_max_height = 200
    GHeroObject.game_data_info.jump_height_speed = 150
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 190
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle")
    add_state_aim("Terra_AO_Blendspace")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "Hitreact_Right")
    add_system_jump("Jump_Start", "Jump_pad", "None", "Jump_PreLand", "Jump_Recovery")
    add_system_knockback("Knockback_back", "Knockback_front", "None")
    add_system_stun("Stun_start", "Stun_Idle", "None")
    add_system_turn("Turn_Left_90", "Turn_Left_180", "Turn_Right_90", "Turn_Right_180")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 300, 50, 300)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 400, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.38, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Primary_Melee_A_slow")
    GHeroObject.add_animation_action("Attack_A_Recovery", "Primary_Melee_A_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_A", "P_Terra_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.38, 0.0, 1.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.34, 0.0)
    GHeroObject.add_animation_action("Attack_B", "Primary_Melee_B_Slow")
    GHeroObject.add_animation_action("Attack_B_Recovery", "Primary_Melee_B_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_B", "P_Terra_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.34, 0.0, 1.0)

    # Skill layer : Attack_C
    GHeroObject.add_skill_property("Attack_C", "T4HeroNormalSkillStat", "Hit", 0.32, 0.0)
    GHeroObject.add_animation_action("Attack_C", "Primary_Melee_C_Slow")
    GHeroObject.add_animation_action("Attack_C_Recovery", "Primary_Melee_C_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_C", "P_Terra_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.32, 0.0, 1.0)

    # Skill layer : Attack_D
    GHeroObject.add_skill_property("Attack_D", "T4HeroNormalSkillStat", "Hit", 0.25, 0.0)
    GHeroObject.add_animation_action("Attack_D", "Primary_Melee_D_Slow")
    GHeroObject.add_animation_action("Attack_D_Recovery", "Primary_Melee_D_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_D", "P_Terra_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.25, 0.0, 1.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.25, 500.0)
    GHeroObject.add_animation_action("Skill_Q", "Primary_Melee_Air")
    GHeroObject.add_particle_action("Skill_Q", "P_Terra_Boom_Shockwave", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.25, 0.0, 1.0)
    GHeroObject.add_movement_action("Skill_Q", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.FRONT, 500, 300.0, 300)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.5, 0.0)
    GHeroObject.add_animation_action("Skill_E", "E_ability")
    GHeroObject.add_particle_action("Skill_E", "P_Terra_Boom_Impacted", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.5, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E", "P_Terra_Boom_ShieldImpact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.5, 0.0, 1.0)

    # Skill layer : Skill_R
    GHeroObject.add_skill_property("Skill_R", "T4HeroCriticalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Skill_R", "R_ending")
    GHeroObject.add_animation_action("Skill_R_Start", "R_helmet_closing")
    GHeroObject.add_animation_action("Skill_R_Loop", "R_helmet_closed_pose")
    GHeroObject.add_animation_action("Skill_R_End", "R_helmet_openning")

    GHeroObject.add_particle_action("Skill_R", "P_Terra_Ultimate", unreal.T4AttachParent.DEFAULT, "Root", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_R_Start", "P_Terra_Ultimate_Activate_Helmet", unreal.T4AttachParent.DEFAULT, "FX_Head", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_R_Loop", "Proto_P_UltimateLoop_Buff", unreal.T4AttachParent.DEFAULT, "Root", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_R_End", "P_Terra_Ultimate_Remove", unreal.T4AttachParent.DEFAULT, "FX_Head", 0.0, 0.0, 1.0)

    # Skill layer : Skill_RMB
    GHeroObject.add_skill_property("Skill_RMB", "T4HeroCriticalSkillStat", "Hit", 0.25, 0.0)
    GHeroObject.add_animation_action("Skill_RMB", "RMB_melee")
    GHeroObject.add_animation_action("Skill_RMB_Start", "RMB_intro")
    GHeroObject.add_animation_action("Skill_RMB_Loop", "RMB_Shield_pose")
    GHeroObject.add_animation_action("Skill_RMB_End", "RMB_end")

    GHeroObject.add_particle_action("Skill_RMB", "P_Terra_Primary_Impact", unreal.T4AttachParent.DEFAULT, "FX_PrimaryImpact", 0.25, 0.0, 1.0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_animation_action("SelectStart", "Emote_HooRah");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_Laugh");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_SharpenAxe");

    return


##
# Drongo
##
def Init_Drongo(target_heros):
    HeroName = "Drongo"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = False


    # GameData
    GHeroObject.game_data_info.race_name = "DarkHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.THROW
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 50
    
    GHeroObject.game_data_info.default_move_speed = 500
    GHeroObject.game_data_info.combat_move_speed = 400
    GHeroObject.game_data_info.sprint_move_speed = 800
    
    GHeroObject.game_data_info.weapon_name = "Pistol"
    
    GHeroObject.game_data_info.jump_max_height = 250
    GHeroObject.game_data_info.jump_height_speed = 200
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 1500
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle_Combat")
    add_state_aim("Idle_Combat_AO")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Primary_Jump_Start", "JumpPad_Default", "Primary_Jump_Fall", "Primary_Jump_Land", "Primary_Jump_Recovery")
    add_system_knockback("JumpPad_Default", "JumpPad_Default", "Primary_Jump_Recovery")
    add_system_stun("Stun_Start", "Stun_Idle", "None")
    add_system_turn("Turn_Left_90", "Turn_Left_180", "Turn_Right_90", "Turn_Right_180")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 500, 100, 500)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 500, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Primary_Fire")
    GHeroObject.add_particle_action("Attack_A", "P_Drongo_Primary_MuzzleFlash", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_A", "P_Drongo_Primary_Projectle_Trail", "P_Drongo_Primary_NoHit", "Muzzle_01", unreal.T4MovementType.STRAIGHT, 2500, 100.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.12, 0.0)
    GHeroObject.add_animation_action("Skill_Q", "Ability_Grenade_Throw")
    GHeroObject.add_animation_action("Skill_Q_Start", "Ability_Grenade_Prep")
    GHeroObject.add_animation_action("Skill_Q_Loop", "Ability_Grenade_Hold")
    GHeroObject.add_particle_action("Skill_Q", "P_Drongo_GrenadeTrail", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.12, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Drongo_Grenade_SilenceSphereLoop", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.12, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q_Loop", "P_Drongo_Grenade_SilenceSphereLoop", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_Q", "P_Drongo_Grenade_SilenceSphereLoop", "P_Drongo_Grenade_Explode", "Muzzle_01", unreal.T4MovementType.PARABOLA, 2000, 500.0)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.0, 250.0)
    GHeroObject.add_animation_action("Skill_E", "Ability_Boomerang_Throw")
    GHeroObject.add_animation_action("Skill_E_Start", "Ability_Boomerang_Prep")
    GHeroObject.add_animation_action("Skill_E_Loop", "Ability_Boomerang_Hold")
    GHeroObject.add_particle_action("Skill_E", "P_Drongo_Boomerang_Out_Flare", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E", "P_Drongo_Boomerang_Out_Shadow", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_E", "P_Drongo_Boomerang_Out_Flare", "P_Drongo_Boomerang_HitWorld", "Muzzle_01", unreal.T4MovementType.PARABOLA, 1500, 100.0)

    # Skill layer : Skill_R
    GHeroObject.add_skill_property("Skill_R", "T4HeroCriticalSkillStat", "Hit", 0.2, 500.0)
    GHeroObject.add_animation_action("Skill_R", "Ability_BazookaFire")
    GHeroObject.add_animation_action("Skill_R_Recovery", "Ability_BazookaLand")
    GHeroObject.add_animation_action("Skill_R_Start", "Ability_BazookaEquip")
    GHeroObject.add_animation_action("Skill_R_Loop", "Ability_BazookaEquippedPose")
    GHeroObject.add_animation_action("Skill_R_End", "Ability_BazookaLand")
    GHeroObject.add_particle_action("Skill_R", "P_Drongo_Ultimate_Explosion", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.2, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_R", "P_Drongo_Ultmate_MuzzleSmoke", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.2, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_R", "P_Drongo_Primary_Projectile_Bullet", "P_Drongo_Ultimate_NoHit", "Muzzle_01", unreal.T4MovementType.STRAIGHT, 2000, 100.0)
    GHeroObject.add_movement_action("Skill_R", unreal.T4MovementType.STRAIGHT, unreal.T4MoveAngleType.BACK, 200, 0, 0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_animation_action("SelectStart", "LevelStartLoop");
    GHeroObject.add_animation_action("Recall", "Recall_Paranoid");

    GHeroObject.add_animation_action("Emote_Good", "Emote_Laugh");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_Taunt");

    return


##
# Morigesh
##
def Init_Morigesh(target_heros):
    HeroName = "Morigesh"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = True


    # GameData
    GHeroObject.game_data_info.race_name = "WhiteHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.THROW
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 50
    
    GHeroObject.game_data_info.default_move_speed = 500
    GHeroObject.game_data_info.combat_move_speed = 400
    GHeroObject.game_data_info.sprint_move_speed = 800
    
    GHeroObject.game_data_info.weapon_name = "Knife"
    
    GHeroObject.game_data_info.jump_max_height = 250
    GHeroObject.game_data_info.jump_height_speed = 200
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 1000
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle")
    add_state_aim("Idle_AimOffset")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Jump_Start", "LaunchPad", "None", "Jump_Preland", "Jump_Recovery")
    add_system_knockback("Knock_Back", "Knock_Back_Bwd", "None")
    add_system_stun("Stun_Start", "Stun_Loop", "None")
    add_system_turn("Turn_Left_90", "Turn_Left_180", "Turn_Right_90", "Turn_Right_180")
    add_system_bound("Bound")
    add_system_resurrect("None")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 500, 100, 500)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 500, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.2, 0.0)
    GHeroObject.add_animation_action("Attack_A", "PrimaryAttack_A_Slow")
    GHeroObject.add_particle_action("Attack_A", "P_Morigesh_Dagger_Glow", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Attack_A", "P_Morigesh_Dagger_Projectile", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.2, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_A", "P_Morigesh_Dagger_Stick", "P_Morigesh_Primary_HitCharacter", "FX_Dagger", unreal.T4MovementType.STRAIGHT, 1700, 50.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.2, 0.0)
    GHeroObject.add_animation_action("Attack_B", "PrimaryAttack_B_Slow")
    GHeroObject.add_particle_action("Attack_B", "P_Morigesh_Dagger_Glow", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Attack_B", "P_Morigesh_Dagger_Projectile", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.2, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_B", "P_Morigesh_Dagger_Stick", "P_Morigesh_Primary_HitCharacter", "FX_Dagger", unreal.T4MovementType.STRAIGHT, 1700, 50.0)

    # Skill layer : Attack_C
    GHeroObject.add_skill_property("Attack_C", "T4HeroNormalSkillStat", "Hit", 0.15, 0.0)
    GHeroObject.add_animation_action("Attack_C", "PrimaryAttack_C_Slow")
    GHeroObject.add_particle_action("Attack_C", "P_Morigesh_Dagger_Glow", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Attack_C", "P_Morigesh_Dagger_Projectile", unreal.T4AttachParent.DEFAULT, "FX_Dagger", 0.15, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_C", "P_Morigesh_Dagger_Stick", "P_Morigesh_Primary_HitCharacter", "FX_Dagger", unreal.T4MovementType.STRAIGHT, 1700, 50.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.34, 0.0)
    GHeroObject.add_animation_action("Skill_Q", "Ability_Q")
    GHeroObject.add_animation_action("Skill_Q_Start", "Ability_Q_Targeting_Start")
    GHeroObject.add_animation_action("Skill_Q_Loop", "Ability_Q_Targeting")
    GHeroObject.add_particle_action("Skill_Q", "P_Morigesh_StabDoll_IMPACT", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.34, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Morigesh_StabDoll_Targeting_Looping", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.0, 0.34, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Morigesh_StabDoll_Trail_01", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.0, 0.34, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Morigesh_StabDoll_Trail_02", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.0, 0.34, 1.0)
    GHeroObject.add_particle_action("Skill_Q_Start", "P_Drongo_Grenade_SilenceSphereLoop", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.7, 0.0, 1.0)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.25, 0.0)
    GHeroObject.add_animation_action("Skill_E", "Ability_E")
    GHeroObject.add_animation_action("Skill_E_Start", "Ability_E_Targeting_Start")
    GHeroObject.add_animation_action("Skill_E_Loop", "Ability_E_Targeting_Idle")
    GHeroObject.add_particle_action("Skill_E", "P_Morigesh_DOT_Impact", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.25, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E", "P_Morigesh_SkillshotAOE_Targeting", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.0, 0.25, 1.0)
    GHeroObject.add_particle_action("Skill_E_Start", "P_Morigesh_SkillshotAOE_Targeting", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.7, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_E", "P_Morigesh_SkillshotAOE_Projectile", "P_Morigesh_SkillshotAOE_Explosion", "FX_BugBall", unreal.T4MovementType.PARABOLA, 1000, 100.0)

    # Skill layer : Skill_RMB
    GHeroObject.add_skill_property("Skill_RMB", "T4HeroCriticalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Skill_RMB", "Ability_RMB")
    GHeroObject.add_particle_action("Skill_RMB", "P_Morigesh_Ultimate_Reveal", unreal.T4AttachParent.DEFAULT, "FX_BugBall", 0.0, 0.0, 1.0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_animation_action("SelectStart", "Emote_SwordSwallow");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_BlowSmoke");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_Taunt");


    # Sprint stance
    init_stance("Sprint")

    add_state_idle("Idle")
    add_state_aim("Idle_AimOffset")
    add_state_fwdrun("SprintFwdSlopeLean", "Sprint_Fwd_Start", "Sprint_Fwd_Stop")
    add_state_bwdrun("SprintBwdSlopeLean", "Sprint_Bwd_Start", "Sprint_Bwd_Stop")

    return


##
# Rampage
##
def Init_Rampage(target_heros):
    HeroName = "Rampage"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = True


    # GameData
    GHeroObject.game_data_info.race_name = "DarkHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.SWING
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 100
    
    GHeroObject.game_data_info.default_move_speed = 350
    GHeroObject.game_data_info.combat_move_speed = 300
    GHeroObject.game_data_info.sprint_move_speed = 700
    
    GHeroObject.game_data_info.weapon_name = "Hand"
    
    GHeroObject.game_data_info.jump_max_height = 200
    GHeroObject.game_data_info.jump_height_speed = 150
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 150
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle")
    add_state_aim("Aim")
    add_state_fwdrun("JogFwdSlopeLean_Quad", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean_Quad", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean_Quad", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean_Quad", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death_A", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Jump_Start", "LaunchPad", "Jump_Fall", "Jump_Mid", "None")
    add_system_knockback("KnockBack", "KnockBack_Bwd", "None")
    add_system_stun("Stun_Start", "Stun_Idle", "None")
    add_system_turn("Turn_Left_90_Quad", "Turn_Left_180_Quad", "Turn_Right_90_Quad", "Turn_Right_180_Quad")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 350, 100, 300)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 400, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.35, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Attack_Melee_A")
    GHeroObject.add_particle_action("Attack_A", "P_Rampage_Melee_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.35, 0.0, 1.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.35, 0.0)
    GHeroObject.add_animation_action("Attack_B", "Attack_Melee_B")
    GHeroObject.add_particle_action("Attack_B", "P_Rampage_Melee_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.35, 0.0, 1.0)

    # Skill layer : Attack_C
    GHeroObject.add_skill_property("Attack_C", "T4HeroCriticalSkillStat", "Hit", 0.38, 0.0)
    GHeroObject.add_animation_action("Attack_C", "Attack_Melee_C")
    GHeroObject.add_particle_action("Attack_C", "P_Rampage_Enraged_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.38, 0.0, 1.0)


    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.17, 100.0)
    GHeroObject.add_animation_action("Skill_Q", "Ability_GroundSmash_End")
    GHeroObject.add_animation_action("Skill_Q_Start", "Ability_GroundSmash_Start")
    GHeroObject.add_animation_action("Skill_Q_Loop", "Ability_GroundSmash_Loop")
    GHeroObject.add_particle_action("Skill_Q", "P_Rampage_SmashArc", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.1, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Rampage_SmashArc", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.1, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q", "P_Rampage_Lunge_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.17, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q_Start", "P_Rampage_LungeEnragedNew", unreal.T4AttachParent.DEFAULT, "Root", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q_Loop", "P_Rampage_Lunge_Impact_Enraged", unreal.T4AttachParent.DEFAULT, "Root", 0.0, 0.0, 1.0)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.35, 0.0)
    GHeroObject.add_animation_action("Skill_E", "Ability_RipNToss_Toss")
    GHeroObject.add_animation_action("Skill_E_Start", "Ability_RipNToss_Rip")
    GHeroObject.add_animation_action("Skill_E_Loop", "Ability_RipNToss_Idle")
    GHeroObject.add_animation_action("Skill_E_End", "Ability_RipNToss_Cancel")

    GHeroObject.add_particle_action("Skill_E_Start", "P_RipNToss_Rip", unreal.T4AttachParent.DEFAULT, "LeftMuzzleName", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E_Loop", "P_Rampage_Rock_Idle", unreal.T4AttachParent.DEFAULT, "LeftMuzzleName", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E", "P_RipNToss_HandImpact", unreal.T4AttachParent.DEFAULT, "LeftMuzzleName", 0.35, 0.0, 1.0)

    # Skill layer : Skill_RMB
    GHeroObject.add_skill_property("Skill_RMB", "T4HeroCriticalSkillStat", "Hit", 0.27, 100)
    GHeroObject.add_animation_action("Skill_RMB", "Ability_RMB_Smash")
    GHeroObject.add_particle_action("Skill_RMB", "P_Rampage_Lunge_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.27, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "P_Rampage_Lunge_Impact", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.51, 0.0, 1.0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");
    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_animation_action("SelectStart", "SelectScreen_Emote");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_Swing_M2");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_Master_Roar_T3");


    # Sprint stance
    init_stance("Sprint")

    add_state_idle("Idle")
    add_state_aim("Aim")
    add_state_fwdrun("JogFwdSlopeLean_Quad", "TravelMode_Fwd_Start", "TravelMode_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean_Quad", "TravelMode_Bwd_Start", "TravelMode_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean_Quad", "None", "None")
    add_state_rightrun("JogRightSlopeLean_Quad", "None", "None")

    return


##
# Revenant
##
def Init_Revenant(target_heros):
    HeroName = "Revenant"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = True
    GHeroObject.has_sprint_stance = False


    # GameData
    GHeroObject.game_data_info.race_name = "WhiteHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.THROW
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 50
    
    GHeroObject.game_data_info.default_move_speed = 500
    GHeroObject.game_data_info.combat_move_speed = 400
    GHeroObject.game_data_info.sprint_move_speed = 800
    
    GHeroObject.game_data_info.weapon_name = "Pistol"
    
    GHeroObject.game_data_info.jump_max_height = 250
    GHeroObject.game_data_info.jump_height_speed = 200
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 1800
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle")
    add_state_aim("Revenant_Idle_AO")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    GHeroObject.add_animation_parameter("BwdRunStop", 0.25)
    GHeroObject.add_animation_parameter("LeftRunStop", 0.7)
    GHeroObject.add_animation_parameter("RightRunStop", 0.15)

    add_system_death("Death_Forward", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Jump_Start", "LaunchPad", "None", "Jump_PreLand", "Jump_Recovery")
    add_system_knockback("Knockback_Fwd", "Knockback_Bwd", "Knockback_Up")
    add_system_stun("Stun_Start", "Stun_Idle", "None")
    add_system_turn("Idle_Turn_90_Left", "Idle_Turn_180_Left", "Idle_Turn_90_Right", "Idle_Turn_180_Right")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 500, 100, 500)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 500, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Primary_Fire_Med")
    GHeroObject.add_particle_action("Attack_A", "P_Revenant_Primary_MuzzleFlash", unreal.T4AttachParent.WORLD, "Muzzle_02", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_A", "P_Revenant_Primary_Trail", "P_Revenant_Primary_HitCharacter", "Muzzle_02", unreal.T4MovementType.PARABOLA, 2800, 25.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.0, 0.0)
    GHeroObject.add_animation_action("Attack_B", "Primary_Fire_Slow")
    GHeroObject.add_particle_action("Attack_B", "P_Revenant_LastShot_MuzzleFlash", unreal.T4AttachParent.WORLD, "Muzzle_02", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Attack_B", "P_Revenant_Primary_Trail", "P_Revenant_Primary_HitCharacter", "Muzzle_02", unreal.T4MovementType.PARABOLA, 2800, 25.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.2, 0.0)
    GHeroObject.add_animation_action("Skill_Q", "Q_Ability")
    GHeroObject.add_animation_action("Skill_Q_Start", "Q_Ability_Targeting_Start")
    GHeroObject.add_animation_action("Skill_Q_Loop", "Q_Ability_Targeting_Loop")
    GHeroObject.add_particle_action("Skill_Q", "P_Revenant_Obliterate_Firing", unreal.T4AttachParent.DEFAULT, "Muzzle_04", 0.2, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_Q_Loop", "P_Revenant_Mark_Ball", unreal.T4AttachParent.DEFAULT, "hand_r_ability_socket", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_Q", "P_Revenant_Obliterate_Trail", "P_Revenant_Obliterate_Hit", "Muzzle_04", unreal.T4MovementType.PARABOLA, 2200, 25.0)

    # Skill layer : Skill_E
    GHeroObject.add_skill_property("Skill_E", "T4HeroCriticalSkillStat", "Hit", 0.2, 200.0)
    GHeroObject.add_animation_action("Skill_E", "E_Ability")
    GHeroObject.add_animation_action("Skill_E_Start", "E_Targeting_Start")
    GHeroObject.add_animation_action("Skill_E_Loop", "E_Targeting_Loop")
    GHeroObject.add_particle_action("Skill_E", "P_Revenant_Mark_End", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.2, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_E_Loop", "P_Revenant_Mark_Ball", unreal.T4AttachParent.DEFAULT, "hand_r_ability_socket", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_E", "P_Revenant_Mark_Trail", "P_Revenant_Mark_Hit", "Muzzle_01", unreal.T4MovementType.PARABOLA, 1600, 25.0)

    # Skill layer : Skill_R
    GHeroObject.add_skill_property("Skill_R", "T4HeroCriticalSkillStat", "Hit", 0.25, 200.0)
    GHeroObject.add_animation_action("Skill_R", "R_Ability")
    GHeroObject.add_animation_action("Skill_R_Start", "R_Ability_Targeting_Start")
    GHeroObject.add_animation_action("Skill_R_Loop", "R_Ability_Targeting_Loop")
    GHeroObject.add_animation_action("Skill_R_End", "R_Ability_Targeting_End")
    GHeroObject.add_particle_action("Skill_R", "P_Revenant_Mark_Hit", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 0.25, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_R_Loop", "P_Revenant_Mark_Targeting", unreal.T4AttachParent.DEFAULT, "hand_r_ability_socket", 0.0, 0.0, 1.0)
    GHeroObject.add_projectile_action("Skill_R", "P_Revenant_Ultimate_Trail", "P_Revenant_Ultimate_Hit", "Muzzle_01", unreal.T4MovementType.PARABOLA, 2000, 25.0)

    # Skill layer : Skill_RMB
    GHeroObject.add_skill_property("Skill_RMB", "T4HeroCriticalSkillStat", "Hit", 0.0, 200.0)
    GHeroObject.add_animation_action("Skill_RMB", "RMB")
    GHeroObject.add_particle_action("Skill_RMB", "P_Revenant_Reload_Insert", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 1.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "P_Revenant_Reload_Insert", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 1.2, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "P_Revenant_Reload_Insert", unreal.T4AttachParent.DEFAULT, "Muzzle_01", 1.4, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "P_Revenant_Reload_Start_Slow", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 1.0, 0.0, 1.0)

     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");

    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_particle_action("LevelStart", "P_Revenant_LevelStart_Gun", unreal.T4AttachParent.DEFAULT, "Muzzle_02", 0.0, 0.2, 1.0)

    GHeroObject.add_animation_action("SelectStart", "Emote_ComeHere");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_I_See_You");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_Spit");
    GHeroObject.add_particle_action("Emote_Bad", "P_Revenant_Spit", unreal.T4AttachParent.DEFAULT, "Root", 0.0, 0.0, 1.0)


    # Sprint stance
    init_stance("NonCombat")

    add_state_idle("Idle_NonCombat_Loop")
    add_state_aim("Revenant_NonCombat_Idle_AO")
    add_state_fwdrun("NonCombat_JogFwdSlopeLean", "NonCombat_Jog_Fwd_Start", "NonCombat_Jog_Fwd_Stop")
    add_state_bwdrun("NonCombat_JogBwdSlopeLean", "NonCombat_Jog_Bwd_Start", "NonCombat_Jog_Bwd_Stop")
    add_state_leftrun("NonCombat_JogLeftSlopeLean", "NonCombat_Jog_Left_Start", "NonCombat_Jog_Left_Stop")
    add_state_rightrun("NonCombat_JogRightSlopeLean", "NonCombat_Jog_Right_Start", "NonCombat_Jog_Right_Stop")

    add_system_jump("NonCombat_Jump_Start", "LaunchPad", "None", "NonCombat_Jump_PreLand", "NonCombat_Jump_Recovery")
    add_system_turn("NonCombat_Idle_Turn_90_Left", "NonCombat_Idle_Turn_180_Left", "NonCombat_Idle_Turn_90_Right", "NonCombat_Idle_Turn_180_Right")

    return


##
# SunWukong
##
def Init_SunWukong(target_heros):
    HeroName = "SunWukong"

    if not HeroName in target_heros and not "All" in target_heros:
        unreal.log(HeroName + " Skipped")
        return

    unreal.log("Add " + HeroName)

    NewHeroObject = unreal.T4HeroObject()
    
    global GHeroObject;
    GHeroObject = NewHeroObject

    GHeroObject.register(HeroName)

    GHeroObject.has_non_combat_stance = False
    GHeroObject.has_sprint_stance = False


    # GameData
    GHeroObject.game_data_info.race_name = "DarkHero"
    GHeroObject.game_data_info.attack_type = unreal.T4GameAttackType.SWING
    
    GHeroObject.game_data_info.bound_height = 200
    GHeroObject.game_data_info.bound_radius = 50
    
    GHeroObject.game_data_info.default_move_speed = 600
    GHeroObject.game_data_info.combat_move_speed = 500
    GHeroObject.game_data_info.sprint_move_speed = 1200
    
    GHeroObject.game_data_info.weapon_name = "Stick"
    
    GHeroObject.game_data_info.jump_max_height = 350
    GHeroObject.game_data_info.jump_height_speed = 300
    
    GHeroObject.game_data_info.sensory_range = 3000

    GHeroObject.game_data_info.min_attack_range = 0
    GHeroObject.game_data_info.max_attack_range = 120
    

    # defualt stance
    init_stance("Default")

    add_state_idle("Idle")
    add_state_aim("Wukong_AO_Blendspace")
    add_state_fwdrun("JogFwdSlopeLean", "Jog_Fwd_Start", "Jog_Fwd_Stop")
    add_state_bwdrun("JogBwdSlopeLean", "Jog_Bwd_Start", "Jog_Bwd_Stop")
    add_state_leftrun("JogLeftSlopeLean", "Jog_Left_Start", "Jog_Left_Stop")
    add_state_rightrun("JogRightSlopeLean", "Jog_Right_Start", "Jog_Right_Stop")

    add_system_death("Death", "None")
    add_system_hit("HitReact_Front", "HitReact_Back", "HitReact_Left", "HitReact_Right")
    add_system_jump("Jump_Start", "Jump_Pad", "Q_Fall_Loop", "Jump_Land", "Jump_Recovery")
    add_system_knockback("Knockback", "Knockfwd", "None")
    add_system_stun("Stun_Start", "Stun_Loop", "None")
    add_system_turn("Idle_Turn_Left_90", "Idle_Turn_Left_180", "Idle_Turn_Right_90", "Idle_Turn_Right_180")
    add_system_bound("Bound")
    add_system_resurrect("Respawn")

    GHeroObject.add_movement_action("Knockback", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.BACK, 600, 100, 600)
    GHeroObject.add_movement_action("Airborne", unreal.T4MovementType.AIRBORNE, unreal.T4MoveAngleType.UP, 0, 600, 300)


    # Effect layer : Hit
    GHeroObject.add_effect_property("Hit", "T4HeroEffectHitStat", unreal.T4GameEffectType.HIT, 0.0, "");

    # Skill layer : Attack_A
    GHeroObject.add_skill_property("Attack_A", "T4HeroNormalSkillStat", "Hit", 0.25, 0.0)
    GHeroObject.add_animation_action("Attack_A", "Primary_Melee_A_Slow")
    GHeroObject.add_animation_action("Attack_A_Recovery", "Primary_Melee_A_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_A", "P_Wukong_Impact", unreal.T4AttachParent.DEFAULT, "FX_Staff_Tip_A", 0.25, 0.0, 1.0)

    # Skill layer : Attack_B
    GHeroObject.add_skill_property("Attack_B", "T4HeroNormalSkillStat", "Hit", 0.25, 0.0)
    GHeroObject.add_animation_action("Attack_B", "Primary_Melee_B_Slow")
    GHeroObject.add_animation_action("Attack_B_Recovery", "Primary_Melee_B_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_B", "P_Wukong_Impact", unreal.T4AttachParent.DEFAULT, "FX_Staff_Tip_A", 0.2, 0.0, 1.0)

    # Skill layer : Attack_C
    GHeroObject.add_skill_property("Attack_C", "T4HeroNormalSkillStat", "Hit", 0.22, 50.0)
    GHeroObject.add_animation_action("Attack_C", "Primary_Melee_C_Slow")
    GHeroObject.add_animation_action("Attack_C_Recovery", "Primary_Melee_C_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_C", "P_Wukong_Impact_Empowered", unreal.T4AttachParent.DEFAULT, "FX_Staff_Tip_A", 0.22, 0.0, 1.0)

    # Skill layer : Attack_D
    GHeroObject.add_skill_property("Attack_D", "T4HeroCriticalSkillStat", "Hit", 0.22, 100.0)
    GHeroObject.add_animation_action("Attack_D", "Primary_Melee_D_Slow")
    GHeroObject.add_animation_action("Attack_D_Recovery", "Primary_Melee_D_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_D", "P_Wukong_Impact_Empowered", unreal.T4AttachParent.DEFAULT, "FX_Staff_Tip_A", 0.28, 0.0, 1.0)

    # Skill layer : Attack_E
    GHeroObject.add_skill_property("Attack_E", "T4HeroCriticalSkillStat", "Hit", 0.15, 0.0)
    GHeroObject.add_animation_action("Attack_E", "Primary_Melee_E_Slow")
    GHeroObject.add_animation_action("Attack_E_Recovery", "Primary_Melee_E_Slow_Recovery")
    GHeroObject.add_particle_action("Attack_E", "P_Wukong_Impact", unreal.T4AttachParent.DEFAULT, "FX_Staff_Tip_A", 0.15, 0.0, 1.0)

    # Skill layer : Skill_Q
    GHeroObject.add_skill_property("Skill_Q", "T4HeroCriticalSkillStat", "Hit", 0.19, 500)
    GHeroObject.add_animation_action("Skill_Q", "Primary_Melee_Air")
    GHeroObject.add_particle_action("Skill_Q", "P_Wukong_Impact_Empowered", unreal.T4AttachParent.DEFAULT, "FX_RocketPunch_r", 0.19, 0.0, 1.0)
    GHeroObject.add_movement_action("Skill_Q", unreal.T4MovementType.PARABOLA, unreal.T4MoveAngleType.FRONT, 500, 250.0, 300)

    # Skill layer : Skill_RMB
    GHeroObject.add_skill_property("Skill_RMB", "T4HeroCriticalSkillStat", "Hit", 0.15, 1000.0)
    GHeroObject.add_animation_action("Skill_RMB", "RMB_Hit")
    GHeroObject.add_animation_action("Skill_RMB_Start", "RMB_Targeting_Start")
    GHeroObject.add_animation_action("Skill_RMB_Loop", "RMB_Targeting_Loop")
    GHeroObject.add_particle_action("Skill_RMB", "p_Offense_Loop_StaffPower", unreal.T4AttachParent.DEFAULT, "FX_Staff_Mid", 0.0, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "p_StaffExtend_Offensive", unreal.T4AttachParent.DEFAULT, "FX_Staff_Mid", 0.15, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB", "p_StaffExtend_Shockwave", unreal.T4AttachParent.DEFAULT, "FX_Staff_Mid", 0.15, 0.0, 1.0)
    GHeroObject.add_particle_action("Skill_RMB_Loop", "p_Offense_Loop_StaffPower", unreal.T4AttachParent.DEFAULT, "FX_Staff_Mid", 0.0, 0.0, 1.0)


     # Skill layer : Etc
    GHeroObject.add_animation_action("Cast", "Cast");

    GHeroObject.add_animation_action("LevelStart", "LevelStart");
    GHeroObject.add_animation_action("SelectStart", "SelectScreen_IdleBreak");
    GHeroObject.add_animation_action("Recall", "Recall");

    GHeroObject.add_animation_action("Emote_Good", "Emote_MonkeyTaunt");
    GHeroObject.add_animation_action("Emote_Bad", "Emote_ComeHere");

    return


def main(target_heros):
    Init_Crunch(target_heros)
    Init_Sparrow(target_heros)
    Init_Terra(target_heros)
    Init_Drongo(target_heros) # Stance 와 Ability 가 특수 처리라 Default 만 처리해 둠. 체크 필요
    Init_Morigesh(target_heros)
    Init_Rampage(target_heros)
    Init_Revenant(target_heros)
    Init_SunWukong(target_heros)
    return;


# py D:\\Tech4Labs\\T4Framework\\T4ParagonHeroMetadata.py All

if __name__ == '__main__':
    main(sys.argv[1])