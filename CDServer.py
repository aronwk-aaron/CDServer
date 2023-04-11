from sqlalchemy import BigInteger, Boolean, CHAR, Column, DateTime, Float, ForeignKey, Identity, Index, Integer, LargeBinary, NCHAR, SmallInteger, String, TEXT, Table, Unicode, text, TINYINT, BLOB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
metadata = Base.metadata


class AICombatBehaviorTypes(Base):
    __tablename__ = 'AICombatBehaviorTypes'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    name = Column(Unicode(50))


class AICombatRoleTypes(Base):
    __tablename__ = 'AICombatRoleTypes'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    name = Column(Unicode(50))

    AICombatRoles = relationship('AICombatRoles', back_populates='AICombatRoleTypes')


class AccessoryDefaultLoc(Base):
    __tablename__ = 'AccessoryDefaultLoc'

    GroupID = Column(Integer, primary_key=True)
    Description = Column(Unicode(50), nullable=False)
    Pos_X = Column(Float(24), nullable=False, server_default=text('((0))'))
    Pos_Y = Column(Float(24), nullable=False, server_default=text('((0))'))
    Pos_Z = Column(Float(24), nullable=False, server_default=text('((0))'))
    Rot_X = Column(Float(24), nullable=False, server_default=text('((0))'))
    Rot_Y = Column(Float(24), nullable=False, server_default=text('((0))'))
    Rot_Z = Column(Float(24), nullable=False, server_default=text('((0))'))

    ItemComponent = relationship('ItemComponent', back_populates='AccessoryDefaultLoc')


class Activities(Base):
    __tablename__ = 'Activities'

    ActivityID = Column(SmallInteger, primary_key=True)
    ActivityName = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    requiresUniqueData = Column(Boolean, nullable=False, server_default=text('((0))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    showUIRewards = Column(Boolean, nullable=False, server_default=text('((1))'))
    Description = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    instanceMapID = Column(Integer)
    minTeams = Column(Integer)
    maxTeams = Column(Integer)
    minTeamSize = Column(Integer)
    maxTeamSize = Column(Integer)
    waitTime = Column(Integer)
    startDelay = Column(Integer)
    leaderboardType = Column(SmallInteger)
    optionalCostLOT = Column(Integer)
    optionalCostCount = Column(Integer)
    CommunityActivityFlagID = Column(Integer)
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))

    ActivityText = relationship('ActivityText', back_populates='Activities')


class ActivityRewards(Base):
    __tablename__ = 'ActivityRewards'

    objectTemplate = Column(Integer, primary_key=True, nullable=False)
    ActivityRewardIndex = Column(Integer, primary_key=True, nullable=False)
    activityRating = Column(Integer, nullable=False, server_default=text('((-1))'))
    LootMatrixIndex = Column(Integer)
    CurrencyIndex = Column(Integer)
    ChallengeRating = Column(Integer)
    description = Column(Unicode(128))


class AnimationIndex(Base):
    __tablename__ = 'AnimationIndex'

    animationGroupID = Column(Integer, primary_key=True)
    description = Column(Unicode(1024))
    groupType = Column(Unicode(1024))

    Animations = relationship('Animations', back_populates='AnimationIndex')


class BaseCombatAIComponent(Base):
    __tablename__ = 'BaseCombatAIComponent'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    ignoreMediator = Column(Boolean, nullable=False, server_default=text('((1))'))
    behaviorType = Column(Integer)
    combatRoundLength = Column(Float(24))
    combatRole = Column(Integer)
    minRoundLength = Column(Float(24))
    maxRoundLength = Column(Float(24))
    tetherSpeed = Column(Float(24))
    pursuitSpeed = Column(Float(24))
    combatStartDelay = Column(Float(24))
    softTetherRadius = Column(Float(24))
    hardTetherRadius = Column(Float(24))
    spawnTimer = Column(Float(24))
    tetherEffectID = Column(Integer)
    aggroRadius = Column(Float(24))


class BehaviorTemplateName(Base):
    __tablename__ = 'BehaviorTemplateName'

    templateID = Column(Integer, primary_key=True)
    name = Column(Unicode, nullable=False)

    BehaviorTemplate = relationship('BehaviorTemplate', back_populates='BehaviorTemplateName')


class BrickColors(Base):
    __tablename__ = 'BrickColors'

    id = Column(Integer, primary_key=True)
    red = Column(Float(24), nullable=False, server_default=text('((0))'))
    green = Column(Float(24), nullable=False, server_default=text('((0))'))
    blue = Column(Float(24), nullable=False, server_default=text('((0))'))
    legopaletteid = Column(Integer, nullable=False, unique=True, server_default=text('((0))'))
    factoryValid = Column(Boolean, nullable=False, server_default=text('((1))'))
    alpha = Column(Float(24))
    description = Column(Unicode(50))
    validTypes = Column(Integer)
    validCharacters = Column(Integer)


t_BrickPhysics = Table(
    'BrickPhysics', metadata,
    Column('LOT', Integer, nullable=False),
    Column('physics_asset', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_BrickView = Table(
    'BrickView', metadata,
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LOT', Integer, nullable=False),
    Column('ItemComponentID', Integer, nullable=False),
    Column('equipLocation', Unicode(64)),
    Column('baseValue', Integer),
    Column('isKitPiece', Boolean, nullable=False),
    Column('rarity', Integer),
    Column('itemType', Integer, nullable=False),
    Column('inLootTable', Boolean, nullable=False),
    Column('inVendor', Boolean, nullable=False),
    Column('isUnique', Boolean, nullable=False),
    Column('isBOP', Boolean, nullable=False),
    Column('isBOE', Boolean, nullable=False),
    Column('reqSpecialtyID', Integer),
    Column('reqSpecRank', Integer),
    Column('reqAchievementID', Integer),
    Column('stackSize', Integer),
    Column('LEGOBrickID', Integer, nullable=False)
)


class BuffDefinitions(Base):
    __tablename__ = 'BuffDefinitions'

    ID = Column(Integer, primary_key=True)
    Name = Column(Unicode(50), nullable=False)
    Priority = Column(Float(24), nullable=False)
    UIIcon = Column(Unicode(50))


class BuffParameters(Base):
    __tablename__ = 'BuffParameters'

    BuffID = Column(Integer, primary_key=True)
    ParameterName = Column(Unicode(50), nullable=False)
    NumberValue = Column(Float(24))
    StringValue = Column(Unicode(128))
    EffectID = Column(Integer)


class Camera(Base):
    __tablename__ = 'Camera'

    camera_name = Column(Unicode(64), primary_key=True)
    pitch_angle_tolerance = Column(Float(24), server_default=text('((0.1))'))
    starting_zoom = Column(Float(24), server_default=text('((28.0))'))
    zoom_return_modifier = Column(Float(24), server_default=text('((15.0))'))
    pitch_return_modifier = Column(Float(24), server_default=text('((1.5))'))
    tether_out_return_modifier = Column(Float(24), server_default=text('((1.5))'))
    tether_in_return_multiplier = Column(Float(24), server_default=text('((5.0))'))
    verticle_movement_dampening_modifier = Column(Float(24), server_default=text('((5.5))'))
    return_from_incline_modifier = Column(Float(24), server_default=text('((1.5))'))
    horizontal_return_modifier = Column(Float(24), server_default=text('((4.5))'))
    yaw_behavior_speed_multiplier = Column(Float(24), server_default=text('((4.0))'))
    camera_collision_padding = Column(Float(24), server_default=text('((0.1))'))
    glide_speed = Column(Float(24), server_default=text('((3.40))'))
    fade_player_min_range = Column(Float(24), server_default=text('((1.56))'))
    min_movement_delta_tolerance = Column(Float(24), server_default=text('((0.0001))'))
    min_glide_distance_tolerance = Column(Float(24), server_default=text('((0.0005))'))
    look_forward_offset = Column(Float(24), server_default=text('((120.0))'))
    look_up_offset = Column(Float(24), server_default=text('((10.0))'))
    minimum_vertical_dampening_distance = Column(Float(24), server_default=text('((4.0))'))
    maximum_vertical_dampening_distance = Column(Float(24), server_default=text('((6.5))'))
    minimum_ignore_jump_distance = Column(Float(24), server_default=text('((5.0))'))
    maximum_ignore_jump_distance = Column(Float(24), server_default=text('((13.0))'))
    maximum_auto_glide_angle = Column(Float(24), server_default=text('((0.5235))'))
    minimum_tether_glide_distance = Column(Float(24), server_default=text('((3.0))'))
    yaw_sign_correction = Column(Float(24), server_default=text('((1.0))'))
    set_1_look_forward_offset = Column(Float(24))
    set_1_look_up_offset = Column(Float(24))
    set_2_look_forward_offset = Column(Float(24))
    set_2_look_up_offset = Column(Float(24))
    set_0_speed_influence_on_dir = Column(Float(24), server_default=text('((1.0))'))
    set_1_speed_influence_on_dir = Column(Float(24), server_default=text('((1.0))'))
    set_2_speed_influence_on_dir = Column(Float(24))
    set_0_angular_relaxation = Column(Float(24), server_default=text('((3.5))'))
    set_1_angular_relaxation = Column(Float(24), server_default=text('((4.5))'))
    set_2_angular_relaxation = Column(Float(24))
    set_0_position_up_offset = Column(Float(24), server_default=text('((8.0))'))
    set_1_position_up_offset = Column(Float(24))
    set_2_position_up_offset = Column(Float(24))
    set_0_position_forward_offset = Column(Float(24), server_default=text('((-25.0))'))
    set_1_position_forward_offset = Column(Float(24))
    set_2_position_forward_offset = Column(Float(24))
    set_0_FOV = Column(Float(24), server_default=text('((60))'))
    set_1_FOV = Column(Float(24), server_default=text('((82.5))'))
    set_2_FOV = Column(Float(24))
    set_0_max_yaw_angle = Column(Float(24))
    set_1_max_yaw_angle = Column(Float(24))
    set_2_max_yaw_angle = Column(Float(24))
    set_1_fade_in_camera_set_change = Column(Integer)
    set_1_fade_out_camera_set_change = Column(Integer)
    set_2_fade_in_camera_set_change = Column(Integer)
    set_2_fade_out_camera_set_change = Column(Integer)
    input_movement_scalar = Column(Float(24), server_default=text('((1))'))
    input_rotation_scalar = Column(Float(24), server_default=text('((1))'))
    input_zoom_scalar = Column(Float(24))
    minimum_pitch_desired = Column(Float(24), server_default=text('((105))'))
    maximum_pitch_desired = Column(Float(24), server_default=text('((100))'))
    minimum_zoom = Column(Float(24), server_default=text('((15))'))
    maximum_zoom = Column(Float(24), server_default=text('((50))'))
    horizontal_rotate_tolerance = Column(Float(24), server_default=text('((0.35))'))
    horizontal_rotate_modifier = Column(Float(24), server_default=text('((2.5))'))


class CelebrationParameters(Base):
    __tablename__ = 'CelebrationParameters'

    id = Column(SmallInteger, Identity(start=1, increment=1), primary_key=True)
    backgroundObject = Column(Integer, nullable=False)
    duration = Column(Float(24), nullable=False)
    celeLeadIn = Column(Float(24), nullable=False)
    celeLeadOut = Column(Float(24), nullable=False)
    cameraPathLOT = Column(Integer, nullable=False)
    pathNodeName = Column(Unicode(50), nullable=False)
    description = Column(Unicode(100))
    animation = Column(Unicode(32))
    subText = Column(Unicode(50))
    mainText = Column(Unicode(50))
    iconID = Column(Integer)
    ambientR = Column(Float(24))
    ambientG = Column(Float(24))
    ambientB = Column(Float(24))
    directionalR = Column(Float(24))
    directionalG = Column(Float(24))
    directionalB = Column(Float(24))
    specularR = Column(Float(24))
    specularG = Column(Float(24))
    specularB = Column(Float(24))
    lightPositionX = Column(Float(24))
    lightPositionY = Column(Float(24))
    lightPositionZ = Column(Float(24))
    blendTime = Column(Float(24))
    fogColorR = Column(Float(24))
    fogColorG = Column(Float(24))
    fogColorB = Column(Float(24))
    musicCue = Column(Unicode(256))
    soundGUID = Column(Unicode(256))
    mixerProgram = Column(Unicode(256))


class ChoiceBuildComponent(Base):
    __tablename__ = 'ChoiceBuildComponent'

    id = Column(Integer, primary_key=True)
    selections = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    imaginationOverride = Column(Integer)


class CollectibleComponent(Base):
    __tablename__ = 'CollectibleComponent'

    id = Column(Integer, primary_key=True)
    requirement_mission = Column(Integer)


class ComponentsRegistry(Base):
    __tablename__ = 'ComponentsRegistry'

    id = Column(Integer, primary_key=True, nullable=False)
    component_type = Column(Integer, primary_key=True, nullable=False, server_default=text('((0))'))
    component_id = Column(Integer, nullable=False)


class ControlSchemes(Base):
    __tablename__ = 'ControlSchemes'

    control_scheme = Column(Integer, primary_key=True)
    scheme_name = Column(Unicode(50))
    rotation_speed = Column(Float(24))
    walk_forward_speed = Column(Float(24))
    walk_backward_speed = Column(Float(24))
    walk_strafe_speed = Column(Float(24))
    walk_strafe_forward_speed = Column(Float(24))
    walk_strafe_backward_speed = Column(Float(24))
    run_backward_speed = Column(Float(24))
    run_strafe_speed = Column(Float(24))
    run_strafe_forward_speed = Column(Float(24))
    run_strafe_backward_speed = Column(Float(24))
    keyboard_zoom_sensitivity = Column(Float(24))
    keyboard_pitch_sensitivity = Column(Float(24))
    keyboard_yaw_sensitivity = Column(Float(24))
    mouse_zoom_wheel_sensitivity = Column(Float(24))
    x_mouse_move_sensitivity_modifier = Column(Float(24))
    y_mouse_move_sensitivity_modifier = Column(Float(24))
    freecam_speed_modifier = Column(Float(24))
    freecam_slow_speed_multiplier = Column(Float(24))
    freecam_fast_speed_multiplier = Column(Float(24))
    freecam_mouse_modifier = Column(Float(24))
    gamepad_pitch_rot_sensitivity = Column(Float(24))
    gamepad_yaw_rot_sensitivity = Column(Float(24))
    gamepad_trigger_sensitivity = Column(Float(24))


class CurrencyIndex(Base):
    __tablename__ = 'CurrencyIndex'

    CurrencyIndex = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    description = Column(NCHAR(128))

    CurrencyTable = relationship('CurrencyTable', back_populates='CurrencyIndex')
    DestructibleComponent = relationship('DestructibleComponent', back_populates='CurrencyIndex_')


class DeletionRestrictions(Base):
    __tablename__ = 'DeletionRestrictions'

    id = Column(Integer, primary_key=True)
    restricted = Column(Boolean, nullable=False, server_default=text('((0))'))
    checkType = Column(Integer, nullable=False, server_default=text('((0))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    ids = Column(CHAR(255, 'SQL_Latin1_General_CP1_CI_AS'))
    failureReason = Column(Unicode(50))
    gate_version = Column(Unicode(32))


class DevModelBehaviors(Base):
    __tablename__ = 'DevModelBehaviors'

    ModelID = Column(Integer, primary_key=True)
    BehaviorID = Column(Integer, nullable=False)


class Emotes(Base):
    __tablename__ = 'Emotes'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    locked = Column(Boolean, nullable=False, server_default=text('((0))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    outputText = Column(Unicode(256))
    targetText = Column(Unicode(256))
    animationName = Column(Unicode(256))
    iconFilename = Column(Unicode(256))
    channel = Column(Unicode(256))
    command = Column(Unicode(256))
    gate_version = Column(Unicode(32))

    SpeedchatMenu = relationship('SpeedchatMenu', back_populates='Emotes')


class EventGating(Base):
    __tablename__ = 'EventGating'

    eventName = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    date_start = Column(DateTime)
    date_end = Column(DateTime)


class ExhibitComponent(Base):
    __tablename__ = 'ExhibitComponent'

    id = Column(Integer, primary_key=True)
    length = Column(Float(24))
    width = Column(Float(24))
    height = Column(Float(24))
    offsetX = Column(Float(24))
    offsetY = Column(Float(24))
    offsetZ = Column(Float(24))
    fReputationSizeMultiplier = Column(Float(24))
    fImaginationCost = Column(Float(24))


class Factions(Base):
    __tablename__ = 'Factions'

    faction = Column(Integer, primary_key=True)
    factionList = Column(Unicode(256), nullable=False)
    factionListFriendly = Column(Boolean, nullable=False)
    description = Column(Unicode(256))
    friendList = Column(Unicode)
    enemyList = Column(Unicode)


class FeatureGating(Base):
    __tablename__ = 'FeatureGating'

    featureName = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True)
    major = Column(Integer, nullable=False)
    current = Column(Integer, nullable=False)
    minor = Column(Integer, nullable=False)
    description = Column(Unicode(255))


class FlairTable(Base):
    __tablename__ = 'FlairTable'

    id = Column(Integer, primary_key=True)
    asset = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class Footsteps(Base):
    __tablename__ = 'Footsteps'

    objectType = Column(Unicode(50), primary_key=True)
    stone = Column(Unicode(128))
    grass = Column(Unicode(128))
    wood = Column(Unicode(128))
    plastic = Column(Unicode(128))
    gravel = Column(Unicode(128))
    mud = Column(Unicode(128))


class Icons(Base):
    __tablename__ = 'Icons'

    IconID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    IconPath = Column(Unicode(200), unique=True)
    IconName = Column(Unicode(64))


class InventoryComponent(Base):
    __tablename__ = 'InventoryComponent'

    id = Column(Integer, primary_key=True, nullable=False)
    itemid = Column(Integer, primary_key=True, nullable=False)
    count = Column(Integer, nullable=False, server_default=text('((1))'))
    equip = Column(Boolean, nullable=False, server_default=text('((0))'))


class ItemEggData(Base):
    __tablename__ = 'ItemEggData'

    id = Column(Integer, primary_key=True)
    chassie_type_id = Column(Integer, nullable=False)


class ItemFoodData(Base):
    __tablename__ = 'ItemFoodData'

    id = Column(Integer, primary_key=True)
    element_1 = Column(Integer)
    element_1_amount = Column(Integer)
    element_2 = Column(Integer)
    element_2_amount = Column(Integer)
    element_3 = Column(Integer)
    element_3_amount = Column(Integer)
    element_4 = Column(Integer)
    element_4_amount = Column(Integer)


class ItemSetSkills(Base):
    __tablename__ = 'ItemSetSkills'

    SkillSetID = Column(Integer, primary_key=True, nullable=False)
    SkillID = Column(Integer, primary_key=True, nullable=False)
    SkillCastType = Column(Integer)


class ItemSets(Base):
    __tablename__ = 'ItemSets'

    setID = Column(Integer, primary_key=True)
    itemIDs = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    description = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    kitType = Column(Integer)
    kitName = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    kitRank = Column(Integer)
    kitImage = Column(Integer)
    skillWith2 = Column(Integer)
    castType2 = Column(Integer)
    skillWith3 = Column(Integer)
    castType3 = Column(Integer)
    skillWith4 = Column(Integer)
    castType4 = Column(Integer)
    skillWith5 = Column(Integer)
    castType5 = Column(Integer)
    skillSetWith2 = Column(Integer)
    skillSetWith3 = Column(Integer)
    skillSetWith4 = Column(Integer)
    skillSetWith5 = Column(Integer)
    skillSetWith6 = Column(Integer)
    gate_version = Column(Unicode(32))


class LUPExhibitComponent(Base):
    __tablename__ = 'LUPExhibitComponent'

    id = Column(Integer, primary_key=True)
    maxXZ = Column(Float(24), nullable=False)
    minXZ = Column(Float(24))
    maxY = Column(Float(24))
    offsetX = Column(Float(24))
    offsetY = Column(Float(24))
    offsetZ = Column(Float(24))


class LUPExhibitModelData(Base):
    __tablename__ = 'LUPExhibitModelData'

    LOT = Column(Integer, primary_key=True)
    minXZ = Column(Float(24), nullable=False)
    maxXZ = Column(Float(24), nullable=False)
    maxY = Column(Float(24), nullable=False)
    description = Column(Unicode(50))
    owner = Column(Unicode(50))


class LUPObjects(Base):
    __tablename__ = 'LUPObjects'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    displayName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    type = Column(SmallInteger, nullable=False)
    isSmashable = Column(Boolean, nullable=False)
    isQuickBuild = Column(Boolean, nullable=False)
    isItem = Column(Boolean, nullable=False)
    interruptible = Column(Boolean)
    activatesSelf = Column(Boolean)
    restTime = Column(SmallInteger)
    completeTime = Column(SmallInteger)
    imaginationCost = Column(SmallInteger)
    prereqImagination = Column(SmallInteger)
    customModules = Column(SmallInteger)
    activityid = Column(SmallInteger)
    soldAtVendor = Column(Boolean)
    isUnique = Column(Boolean)
    bindOnPickup = Column(Boolean)
    clientScript = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    serverScript = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))


class LUPZoneIDs(Base):
    __tablename__ = 'LUPZoneIDs'

    zoneID = Column(Integer, primary_key=True)


class LanguageType(Base):
    __tablename__ = 'LanguageType'

    LanguageID = Column(Integer, primary_key=True)
    LanguageDescription = Column(Unicode(255), nullable=False)

    TextLanguage = relationship('TextLanguage', back_populates='LanguageType')


t_LootItemsByMatrix = Table(
    'LootItemsByMatrix', metadata,
    Column('LootMatrixIndex', Integer, nullable=False),
    Column('LootTableIndex', Integer, nullable=False),
    Column('itemid', Integer, nullable=False)
)


class LootMatrixIndex(Base):
    __tablename__ = 'LootMatrixIndex'

    LootMatrixIndex = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    inNpcEditor = Column(Boolean, nullable=False)
    description = Column(NCHAR(128))

    DestructibleComponent = relationship('DestructibleComponent', back_populates='LootMatrixIndex_')
    LootMatrix = relationship('LootMatrix', back_populates='LootMatrixIndex_')
    VendorComponent = relationship('VendorComponent', back_populates='LootMatrixIndex_')


class LootTableIndex(Base):
    __tablename__ = 'LootTableIndex'

    LootTableIndex = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    description = Column(NCHAR(128))

    LootMatrix = relationship('LootMatrix', back_populates='LootTableIndex_')
    LootTable = relationship('LootTable', back_populates='LootTableIndex_')


class MinifigComponent(Base):
    __tablename__ = 'MinifigComponent'

    id = Column(Integer, primary_key=True)
    head = Column(Integer)
    chest = Column(Integer)
    legs = Column(Integer)
    hairstyle = Column(Integer)
    haircolor = Column(Integer)
    chestdecal = Column(Integer)
    headcolor = Column(Integer)
    lefthand = Column(Integer)
    righthand = Column(Integer)
    eyebrowstyle = Column(Integer)
    eyesstyle = Column(Integer)
    mouthstyle = Column(Integer)


class MinifigDecalsEyebrows(Base):
    __tablename__ = 'MinifigDecals_Eyebrows'

    ID = Column(Integer, primary_key=True)
    CharacterCreateValid = Column(Boolean, nullable=False)
    male = Column(Boolean, nullable=False)
    female = Column(Boolean, nullable=False)
    High_path = Column(Unicode(255))
    Low_path = Column(Unicode(255))


class MinifigDecalsEyes(Base):
    __tablename__ = 'MinifigDecals_Eyes'

    ID = Column(Integer, primary_key=True)
    CharacterCreateValid = Column(Boolean, nullable=False)
    male = Column(Boolean, nullable=False)
    female = Column(Boolean, nullable=False)
    High_path = Column(Unicode(255))
    Low_path = Column(Unicode(255))


class MinifigDecalsLegs(Base):
    __tablename__ = 'MinifigDecals_Legs'

    ID = Column(Integer, primary_key=True)
    High_path = Column(Unicode(255), nullable=False)
    _description = Column(Unicode(255))


class MinifigDecalsMouths(Base):
    __tablename__ = 'MinifigDecals_Mouths'

    ID = Column(Integer, primary_key=True)
    CharacterCreateValid = Column(Boolean, nullable=False)
    male = Column(Boolean, nullable=False)
    female = Column(Boolean, nullable=False)
    High_path = Column(Unicode(255))
    Low_path = Column(Unicode(255))


class MinifigDecalsTorsos(Base):
    __tablename__ = 'MinifigDecals_Torsos'

    ID = Column(Integer, primary_key=True)
    CharacterCreateValid = Column(Boolean, nullable=False)
    male = Column(Boolean, nullable=False, server_default=text('((0))'))
    female = Column(Boolean, nullable=False, server_default=text('((0))'))
    High_path = Column(Unicode(255))
    _description = Column(Unicode(256))


class MissionEmail(Base):
    __tablename__ = 'MissionEmail'

    ID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    messageType = Column(Integer, nullable=False)
    notificationGroup = Column(Integer, nullable=False)
    missionID = Column(Integer, nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    senderName = Column(Unicode(256))
    subjectText = Column(Unicode(1024))
    bodyText = Column(Unicode(1024))
    attachmentLOT = Column(Integer)
    announceText = Column(Unicode(1024))
    gate_version = Column(Unicode(32))


class MissionNPCComponent(Base):
    __tablename__ = 'MissionNPCComponent'

    id = Column(Integer, primary_key=True, nullable=False)
    missionID = Column(Integer, primary_key=True, nullable=False)
    offersMission = Column(Boolean, nullable=False, server_default=text('((1))'))
    acceptsMission = Column(Boolean, nullable=False, server_default=text('((1))'))
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class Missions(Base):
    __tablename__ = 'Missions'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    isChoiceReward = Column(Boolean, nullable=False, server_default=text('((0))'))
    reward_item1 = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item1_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item2 = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item2_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item3 = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item3_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item4 = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item4_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_emote = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_maximagination = Column(Integer, nullable=False, server_default=text('((0))'))
    reward_maxhealth = Column(Integer, nullable=False, server_default=text('((0))'))
    repeatable = Column(Boolean, nullable=False, server_default=text('((0))'))
    reward_item1_repeatable = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item1_repeat_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item2_repeatable = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item2_repeat_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item3_repeatable = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item3_repeat_count = Column(Integer, nullable=False, server_default=text('((1))'))
    reward_item4_repeatable = Column(Integer, nullable=False, server_default=text('((-1))'))
    reward_item4_repeat_count = Column(Integer, nullable=False, server_default=text('((1))'))
    isMission = Column(Boolean, nullable=False, server_default=text('((-1))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    inMOTD = Column(Boolean, nullable=False, server_default=text('((0))'))
    isRandom = Column(Boolean, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    defined_type = Column(Unicode(128))
    defined_subtype = Column(Unicode(128))
    UISortOrder = Column(Integer)
    offer_objectID = Column(Integer)
    target_objectID = Column(Integer)
    reward_currency = Column(BigInteger)
    LegoScore = Column(Integer)
    reward_reputation = Column(BigInteger)
    reward_emote2 = Column(Integer)
    reward_emote3 = Column(Integer)
    reward_emote4 = Column(Integer)
    reward_maxinventory = Column(Integer)
    reward_maxmodel = Column(Integer)
    reward_maxwidget = Column(Integer)
    reward_maxwallet = Column(BigInteger)
    reward_currency_repeatable = Column(BigInteger)
    time_limit = Column(Integer)
    missionIconID = Column(Integer)
    prereqMissionID = Column(Unicode(512))
    cooldownTime = Column(BigInteger)
    randomPool = Column(Unicode(512))
    UIPrereqID = Column(Integer)
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('test')"))
    HUDStates = Column(Unicode(128))
    reward_bankinventory = Column(Integer)

    MissionTasks = relationship('MissionTasks', back_populates='Missions')


class ModelBehavior(Base):
    __tablename__ = 'ModelBehavior'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    definitionXMLfilename = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)


class ModularBuildComponent(Base):
    __tablename__ = 'ModularBuildComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    buildType = Column(Integer, nullable=False)
    xml = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    createdLOT = Column(Integer)
    createdPhysicsID = Column(Integer)
    AudioEventGUID_Snap = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventGUID_Complete = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventGUID_Present = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))


class ModuleComponent(Base):
    __tablename__ = 'ModuleComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    partCode = Column(Integer, nullable=False)
    buildType = Column(Integer, nullable=False)
    xml = Column(TEXT(2147483647, 'SQL_Latin1_General_CP1_CI_AS'))
    primarySoundGUID = Column(Unicode(50))
    assembledEffectID = Column(Integer)


class MotionFX(Base):
    __tablename__ = 'MotionFX'

    id = Column(Integer, primary_key=True)
    typeID = Column(Integer, nullable=False)
    slamVelocity = Column(Float(24))
    addVelocity = Column(Float(24))
    duration = Column(Float(24))
    destGroupName = Column(Unicode(128))
    startScale = Column(Float(24))
    endScale = Column(Float(24))
    velocity = Column(Float(24))
    distance = Column(Float(24))

    BehaviorEffect = relationship('BehaviorEffect', back_populates='MotionFX')


t_MovableObjectsThatDontHaveScript = Table(
    'MovableObjectsThatDontHaveScript', metadata,
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('Expr1', Integer)
)


t_MovableScriptedObjects = Table(
    'MovableScriptedObjects', metadata,
    Column('id', Integer, nullable=False),
    Column('component_type', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS'))
)


class MovementAIComponent(Base):
    __tablename__ = 'MovementAIComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    MovementType = Column(Unicode(50), nullable=False)
    WanderChance = Column(Float(24))
    WanderDelayMin = Column(Float(24))
    WanderDelayMax = Column(Float(24))
    WanderSpeed = Column(Float(24))
    WanderRadius = Column(Float(24))
    attachedPath = Column(Unicode(256))
    Description = Column(Unicode(256))


class NPCCreateData(Base):
    __tablename__ = 'NPCCreateData'

    npcCreateID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    NPCtype = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    Subtype = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    SubSubType = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    animationGroupType = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    RenderAsset = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ScriptReference = Column(Integer)
    DestructableReference = Column(Integer)
    PhysicsReference = Column(Integer)
    PhysicsTypeRef = Column(Integer)
    VendorReference = Column(Integer)


class NpcIcons(Base):
    __tablename__ = 'NpcIcons'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    isClickable = Column(Boolean, nullable=False)
    rotateToFace = Column(Boolean, nullable=False, server_default=text('((0))'))
    color = Column(Integer)
    offset = Column(Float(24))
    LOT = Column(Integer)
    scale = Column(Float(24), server_default=text('((1))'))
    description = Column(Unicode(255))
    compositeHorizOffset = Column(Float(24))
    compositeVertOffset = Column(Float(24))
    compositeScale = Column(Float(24))
    compositeConnectionNode = Column(Unicode(255))
    compositeLOTMultiMission = Column(Integer)
    compositeLOTMultiMissionVentor = Column(Integer)


class ObjectBehaviorXREF(Base):
    __tablename__ = 'ObjectBehaviorXREF'

    LOT = Column(Integer, primary_key=True)
    behaviorID1 = Column(BigInteger)
    behaviorID2 = Column(BigInteger)
    behaviorID3 = Column(BigInteger)
    behaviorID4 = Column(BigInteger)
    behaviorID5 = Column(BigInteger)
    type = Column(SmallInteger)


class ObjectBehaviors(Base):
    __tablename__ = 'ObjectBehaviors'

    BehaviorID = Column(BigInteger, primary_key=True)
    xmldata = Column(XML, nullable=False)


class Objects(Base):
    __tablename__ = 'Objects'

    id = Column(Integer, primary_key=True)
    placeable = Column(Boolean, nullable=False, server_default=text('((1))'))
    type = Column(Unicode(64), nullable=False, server_default=text("('')"))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    HQ_valid = Column(Boolean, nullable=False, server_default=text('((0))'))
    name = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    description = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    npcTemplateID = Column(Integer)
    displayName = Column(Unicode(256))
    interactionDistance = Column(Float(24))
    nametag = Column(Boolean, server_default=text('((0))'))
    _internalNotes = Column(Unicode(256))
    gate_version = Column(Unicode(32))

    BrickIDTable = relationship('BrickIDTable', back_populates='Objects')
    CurrencyDenominations = relationship('CurrencyDenominations', back_populates='Objects')
    ObjectSkills = relationship('ObjectSkills', back_populates='Objects')


class PackageComponent(Base):
    __tablename__ = 'PackageComponent'

    id = Column(Integer, primary_key=True)
    LootMatrixIndex = Column(Integer, nullable=False)
    packageType = Column(Integer, nullable=False, server_default=text('((0))'))


class PetAbilities(Base):
    __tablename__ = 'PetAbilities'

    id = Column(Integer, primary_key=True)
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    AbilityName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ImaginationCost = Column(Integer)
    DisplayName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))


class PetComponent(Base):
    __tablename__ = 'PetComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    description = Column(Unicode(256))
    minTameUpdateTime = Column(Float(24))
    maxTameUpdateTime = Column(Float(24))
    percentTameChance = Column(Float(24))
    tamability = Column(Float(24))
    elementType = Column(Integer)
    walkSpeed = Column(Float(24))
    runSpeed = Column(Float(24))
    sprintSpeed = Column(Float(24))
    idleTimeMin = Column(Float(24))
    idleTimeMax = Column(Float(24))
    eggLotId = Column(Integer)
    petForm = Column(Integer)
    imaginationDrainRate = Column(Float(24))
    AudioMetaEventSet = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    playerFlag = Column(Integer)


class PetNestComponent(Base):
    __tablename__ = 'PetNestComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    ElementalType = Column(Integer)


class PhysicsComponent(Base):
    __tablename__ = 'PhysicsComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    static = Column(Float(24), nullable=False)
    jump = Column(Float(24), nullable=False)
    doublejump = Column(Float(24), nullable=False, server_default=text('((0))'))
    pcShapeType = Column(Integer, nullable=False)
    collisionGroup = Column(Integer, nullable=False)
    airSpeed = Column(Float(24), nullable=False, server_default=text('((10))'))
    physics_asset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    speed = Column(Float(24))
    rotSpeed = Column(Float(24))
    playerHeight = Column(Float(24))
    playerRadius = Column(Float(24))
    boundaryAsset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    jumpAirSpeed = Column(Float(24), server_default=text('((25))'))
    friction = Column(Float(24))
    gravityVolumeAsset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class PlayerFlags(Base):
    __tablename__ = 'PlayerFlags'

    id = Column(Integer, primary_key=True)
    SessionOnly = Column(Boolean, nullable=False, server_default=text('((0))'))
    OnlySetByServer = Column(Boolean, nullable=False, server_default=text('((0))'))
    description = Column(Unicode(50))


class PlayerStatistics(Base):
    __tablename__ = 'PlayerStatistics'

    statID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    statStr = Column(Unicode(50))
    description = Column(Unicode(200))
    sortOrder = Column(Integer)
    gate_version = Column(Unicode(32))


class PreconditionTypes(Base):
    __tablename__ = 'PreconditionTypes'

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(50))


class Preconditions(Base):
    __tablename__ = 'Preconditions'

    id = Column(Integer, primary_key=True)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    validContexts = Column(BigInteger, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    type = Column(Integer)
    description = Column(Unicode(50))
    targetLOT = Column(Unicode(250))
    targetGroup = Column(Unicode(50))
    targetCount = Column(Integer)
    FailureReason = Column(Unicode(255))
    iconID = Column(Integer)
    gate_version = Column(Unicode(32))


class PropertyTemplate(Base):
    __tablename__ = 'PropertyTemplate'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    mapID = Column(Integer, nullable=False)
    spawnName = Column(Unicode(50), nullable=False)
    type = Column(TINYINT, nullable=False, server_default=text('((0))'))
    sizecode = Column(TINYINT, nullable=False, server_default=text('((0))'))
    minimumPrice = Column(Integer, nullable=False, server_default=text('((0))'))
    rentDuration = Column(Integer, nullable=False, server_default=text('((0))'))
    cloneLimit = Column(Integer, nullable=False, server_default=text('((1))'))
    durationType = Column(TINYINT, nullable=False, server_default=text('((3))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    reputationPerMinute = Column(Integer, nullable=False, server_default=text('((1.0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    vendorMapID = Column(Integer)
    path = Column(Unicode(4000))
    name = Column(Unicode(50))
    description = Column(Unicode(300))
    achievementRequired = Column(SmallInteger, server_default=text('((0))'))
    zoneX = Column(Float(24), server_default=text('((0))'))
    zoneY = Column(Float(24))
    zoneZ = Column(Float(24))
    maxBuildHeight = Column(Float(24))
    gate_version = Column(Unicode(32))


class ProximityMonitorComponent(Base):
    __tablename__ = 'ProximityMonitorComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    LoadOnClient = Column(Boolean, nullable=False, server_default=text('((0))'))
    LoadOnServer = Column(Boolean, nullable=False, server_default=text('((0))'))
    Proximities = Column(Unicode(50))


class ProximityTypes(Base):
    __tablename__ = 'ProximityTypes'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    Name = Column(Unicode(50), nullable=False)
    PassiveChecks = Column(Boolean, nullable=False, server_default=text('((1))'))
    LoadOnClient = Column(Boolean, nullable=False, server_default=text('((0))'))
    LoadOnServer = Column(Boolean, nullable=False, server_default=text('((0))'))
    Radius = Column(Integer)
    CollisionGroup = Column(Integer)
    IconID = Column(Integer)


class RacingModuleComponent(Base):
    __tablename__ = 'RacingModuleComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    topSpeed = Column(Float(24))
    acceleration = Column(Float(24))
    handling = Column(Float(24))
    stability = Column(Float(24))
    imagination = Column(Float(24))


class RarityTableIndex(Base):
    __tablename__ = 'RarityTableIndex'

    RarityTableIndex = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    description = Column(NCHAR(128))

    LootMatrix = relationship('LootMatrix', back_populates='RarityTableIndex_')
    RarityTable = relationship('RarityTable', back_populates='RarityTableIndex_')


class RebuildComponent(Base):
    __tablename__ = 'RebuildComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reset_time = Column(Float(24), nullable=False, server_default=text('((20.0))'))
    take_imagination = Column(Integer, nullable=False, server_default=text('((1))'))
    interruptible = Column(Boolean, nullable=False, server_default=text('((0))'))
    self_activator = Column(Boolean, nullable=False, server_default=text('((0))'))
    time_before_smash = Column(Float(24), nullable=False, server_default=text('((10))'))
    complete_time = Column(Float(24))
    custom_modules = Column(CHAR(255, 'SQL_Latin1_General_CP1_CI_AS'))
    activityID = Column(Integer)
    post_imagination_cost = Column(Integer)


class RebuildSections(Base):
    __tablename__ = 'RebuildSections'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    rebuildID = Column(Integer, nullable=False)
    objectID = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False, server_default=text('((0))'))
    bPlaced = Column(Boolean, nullable=False, server_default=text('((0))'))
    offset_x = Column(Float(24))
    offset_y = Column(Float(24))
    offset_z = Column(Float(24))
    fall_angle_x = Column(Float(24))
    fall_angle_y = Column(Float(24))
    fall_angle_z = Column(Float(24))
    fall_height = Column(Float(24))
    requires_list = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))


class ReleaseVersion(Base):
    __tablename__ = 'Release_Version'

    ReleaseVersion = Column(Unicode(32), primary_key=True)
    ReleaseDate = Column(DateTime, nullable=False, server_default=text('(getutcdate())'))


class RenderComponent(Base):
    __tablename__ = 'RenderComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    fade = Column(Boolean, nullable=False, server_default=text('((1))'))
    usedropshadow = Column(Boolean, nullable=False, server_default=text('((0))'))
    preloadAnimations = Column(Boolean, nullable=False, server_default=text('((0))'))
    fadeInTime = Column(Float(24), nullable=False, server_default=text('((1))'))
    maxShadowDistance = Column(Float(24), nullable=False, server_default=text('((0))'))
    ignoreCameraCollision = Column(Boolean, nullable=False, server_default=text('((0))'))
    gradualSnap = Column(Boolean, nullable=False, server_default=text('((0))'))
    staticBillboard = Column(Boolean, nullable=False, server_default=text('((0))'))
    render_asset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    icon_asset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    IconID = Column(Integer)
    shader_id = Column(Integer)
    effect1 = Column(Integer)
    effect2 = Column(Integer)
    effect3 = Column(Integer)
    effect4 = Column(Integer)
    effect5 = Column(Integer)
    effect6 = Column(Integer)
    footstepType = Column(Unicode(50))
    animationGroupIDs = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    renderComponentLOD1 = Column(Integer)
    renderComponentLOD2 = Column(Integer)
    animationFlag = Column(Integer)
    AudioMetaEventSet = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    billboardHeight = Column(Float(24))
    LXFMLFolder = Column(Unicode(255))


class RenderComponentFlash(Base):
    __tablename__ = 'RenderComponentFlash'

    id = Column(Integer, nullable=False, index=True)
    interactive = Column(Boolean, nullable=False)
    animated = Column(Boolean, nullable=False)
    nodeName = Column(Unicode(50), nullable=False)
    flashPath = Column(Unicode(128), nullable=False)
    _uid = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    elementName = Column(Unicode(50))


class RenderComponentWrapper(Base):
    __tablename__ = 'RenderComponentWrapper'

    id = Column(Integer, primary_key=True)
    defaultWrapperAsset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class RenderIconAssets(Base):
    __tablename__ = 'RenderIconAssets'

    id = Column(SmallInteger, Identity(start=1, increment=1), primary_key=True)
    icon_asset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    blank_column = Column(NCHAR(10))


class ReputationRewards(Base):
    __tablename__ = 'ReputationRewards'

    repLevel = Column(Integer, primary_key=True, nullable=False)
    sublevel = Column(SmallInteger, primary_key=True, nullable=False)
    reputation = Column(Float(24), nullable=False)


class RewardCodes(Base):
    __tablename__ = 'RewardCodes'

    id = Column(Integer, primary_key=True)
    code = Column(Unicode(50), nullable=False)
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    subjectText = Column(Unicode(1024))
    bodyText = Column(Unicode(1024))
    attachmentLOT = Column(Integer)
    gate_version = Column(Unicode(32))


t_SampleItemView = Table(
    'SampleItemView', metadata,
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LOT', Integer, nullable=False),
    Column('ItemComponentID', Integer, nullable=False),
    Column('equipLocation', Unicode(64)),
    Column('baseValue', Integer),
    Column('isKitPiece', Boolean, nullable=False),
    Column('rarity', Integer),
    Column('itemType', Integer, nullable=False),
    Column('inLootTable', Boolean, nullable=False),
    Column('inVendor', Boolean, nullable=False),
    Column('isUnique', Boolean, nullable=False),
    Column('isBOP', Boolean, nullable=False),
    Column('isBOE', Boolean, nullable=False),
    Column('reqSpecialtyID', Integer),
    Column('reqSpecRank', Integer),
    Column('reqAchievementID', Integer),
    Column('stackSize', Integer),
    Column('color1', Integer),
    Column('decal', Integer)
)


t_SamplePhysicsView = Table(
    'SamplePhysicsView', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('physics_asset', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PhysicsID', Integer, nullable=False),
    Column('speed', Float(24)),
    Column('rotSpeed', Float(24)),
    Column('jump', Float(24), nullable=False),
    Column('doublejump', Float(24), nullable=False),
    Column('playerHeight', Float(24)),
    Column('playerRadius', Float(24)),
    Column('pcShapeType', Integer, nullable=False),
    Column('collisionGroup', Integer, nullable=False),
    Column('airSpeed', Float(24), nullable=False),
    Column('boundaryAsset', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('component_type', Integer, nullable=False),
    Column('static', Float(24), nullable=False),
    Column('jumpAirSpeed', Float(24))
)


t_SampleRenderView = Table(
    'SampleRenderView', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('effect1', Integer),
    Column('effect2', Integer),
    Column('effect3', Integer),
    Column('RenderID', Integer, nullable=False),
    Column('render_asset', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('shader_id', Integer),
    Column('icon_asset', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('effect4', Integer),
    Column('effect5', Integer),
    Column('effect6', Integer),
    Column('footstepType', Unicode(50)),
    Column('fade', Boolean, nullable=False),
    Column('usedropshadow', Boolean, nullable=False),
    Column('preloadAnimations', Boolean, nullable=False),
    Column('fadeInTime', Float(24), nullable=False),
    Column('maxShadowDistance', Float(24), nullable=False),
    Column('ignoreCameraCollision', Boolean, nullable=False),
    Column('animationGroupIDs', String(255, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_SampleSCriptComponent = Table(
    'SampleSCriptComponent', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('script_name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('client_script_name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('component_type', Integer, nullable=False),
    Column('SCriptID', Integer, nullable=False)
)


t_SampleViewComponents = Table(
    'SampleViewComponents', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('component_type', Integer, nullable=False),
    Column('label', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('component_id', Integer, nullable=False)
)


class SceneTable(Base):
    __tablename__ = 'SceneTable'

    sceneID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    sceneName = Column(Unicode(256))


class ScriptComponent(Base):
    __tablename__ = 'ScriptComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    script_name = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    client_script_name = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class SmashableChain(Base):
    __tablename__ = 'SmashableChain'

    chainIndex = Column(Integer, primary_key=True, nullable=False, server_default=text('((0))'))
    chainLevel = Column(Integer, primary_key=True, nullable=False, server_default=text('((0))'))
    smashCount = Column(Integer, nullable=False, server_default=text('((1))'))
    chainStepID = Column(Integer, Identity(start=1, increment=1), nullable=False)
    lootMatrixID = Column(Integer)
    rarityTableIndex = Column(Integer)
    currencyIndex = Column(Integer)
    currencyLevel = Column(Integer)
    timeLimit = Column(Integer, server_default=text('((0))'))


class SmashableChainIndex(Base):
    __tablename__ = 'SmashableChainIndex'

    id = Column(Integer, primary_key=True)
    targetGroup = Column(Unicode(256), nullable=False)
    description = Column(Unicode(128))
    continuous = Column(Integer)


class SmashableComponent(Base):
    __tablename__ = 'SmashableComponent'

    id = Column(Integer, primary_key=True)
    LootMatrixIndex = Column(Integer, nullable=False)


class SmashableElements(Base):
    __tablename__ = 'SmashableElements'

    elementID = Column(Integer, primary_key=True)
    dropWeight = Column(Integer)


class SurfaceType(Base):
    __tablename__ = 'SurfaceType'

    SurfaceType = Column(Integer, primary_key=True, server_default=text('((0))'))
    Name = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    FootstepNDAudioMetaEventSetName = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))


class TamingBuildPuzzles(Base):
    __tablename__ = 'TamingBuildPuzzles'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    PuzzleModelLot = Column(Integer, nullable=False)
    NPCLot = Column(Integer, nullable=False)
    Duration = Column(Float(24), nullable=False, server_default=text('((45.0))'))
    imagCostPerBuild = Column(Integer, nullable=False, server_default=text('((1))'))
    ValidPiecesLXF = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    InvalidPiecesLXF = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    Difficulty = Column(Integer)
    Timelimit = Column(Integer)
    NumValidPieces = Column(Integer)
    TotalNumPieces = Column(Integer)
    ModelName = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FullModelLXF = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class TextDescription(Base):
    __tablename__ = 'TextDescription'

    TextID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    TestDescription = Column(Unicode(1024), nullable=False)


class TrailEffects(Base):
    __tablename__ = 'TrailEffects'

    trailID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    cardlifetime = Column(Float(24), nullable=False, server_default=text('((0))'))
    colorlifetime = Column(Float(24), nullable=False, server_default=text('((0))'))
    minTailFade = Column(Float(24), nullable=False, server_default=text('((0))'))
    tailFade = Column(Float(24), nullable=False, server_default=text('((0))'))
    birthDelay = Column(Float(24), nullable=False, server_default=text('((0))'))
    deathDelay = Column(Float(24), nullable=False, server_default=text('((0))'))
    texLength = Column(Float(24), nullable=False, server_default=text('((0))'))
    texWidth = Column(Float(24), nullable=False, server_default=text('((0))'))
    startColorR = Column(Float(24), nullable=False, server_default=text('((0))'))
    startColorG = Column(Float(24), nullable=False, server_default=text('((0))'))
    startColorB = Column(Float(24), nullable=False, server_default=text('((0))'))
    startColorA = Column(Float(24), nullable=False, server_default=text('((0))'))
    middleColorR = Column(Float(24), nullable=False, server_default=text('((0))'))
    middleColorG = Column(Float(24), nullable=False, server_default=text('((0))'))
    middleColorB = Column(Float(24), nullable=False, server_default=text('((0))'))
    middleColorA = Column(Float(24), nullable=False, server_default=text('((0))'))
    endColorR = Column(Float(24), nullable=False, server_default=text('((0))'))
    endColorG = Column(Float(24), nullable=False, server_default=text('((0))'))
    endColorB = Column(Float(24), nullable=False, server_default=text('((0))'))
    endColorA = Column(Float(24), nullable=False, server_default=text('((0))'))
    description = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    textureName = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    blendmode = Column(SmallInteger)
    max_particles = Column(Integer)
    bone1 = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    bone2 = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))

    BehaviorEffect = relationship('BehaviorEffect', back_populates='TrailEffects')


class UGBehaviorSounds(Base):
    __tablename__ = 'UGBehaviorSounds'

    id = Column(Integer, primary_key=True)
    guid = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    name = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    gate_version = Column(Unicode(32))


class VehiclePhysics(Base):
    __tablename__ = 'VehiclePhysics'

    id = Column(Integer, primary_key=True)
    fGravityScale = Column(Float(24), nullable=False)
    fMass = Column(Float(24), nullable=False)
    fChassisFriction = Column(Float(24), nullable=False)
    fMaxSpeed = Column(Float(24), nullable=False)
    fEngineTorque = Column(Float(24), nullable=False)
    fBrakeFrontTorque = Column(Float(24), nullable=False)
    fBrakeRearTorque = Column(Float(24), nullable=False)
    fBrakeMinInputToBlock = Column(Float(24), nullable=False)
    fBrakeMinTimeToBlock = Column(Float(24), nullable=False)
    fSteeringMaxAngle = Column(Float(24), nullable=False)
    fSteeringSpeedLimitForMaxAngle = Column(Float(24), nullable=False)
    fSteeringMinAngle = Column(Float(24), nullable=False)
    fFwdBias = Column(Float(24), nullable=False)
    fFrontTireFriction = Column(Float(24), nullable=False)
    fRearTireFriction = Column(Float(24), nullable=False)
    fFrontTireFrictionSlide = Column(Float(24), nullable=False)
    fRearTireFrictionSlide = Column(Float(24), nullable=False)
    fFrontTireSlipAngle = Column(Float(24), nullable=False)
    fRearTireSlipAngle = Column(Float(24), nullable=False)
    fWheelWidth = Column(Float(24), nullable=False)
    fWheelRadius = Column(Float(24), nullable=False)
    fWheelMass = Column(Float(24), nullable=False)
    fReorientPitchStrength = Column(Float(24), nullable=False)
    fReorientRollStrength = Column(Float(24), nullable=False)
    fSuspensionLength = Column(Float(24), nullable=False)
    fSuspensionStrength = Column(Float(24), nullable=False)
    fSuspensionDampingCompression = Column(Float(24), nullable=False)
    fSuspensionDampingRelaxation = Column(Float(24), nullable=False)
    iChassisCollisionGroup = Column(Integer, nullable=False)
    fNormalSpinDamping = Column(Float(24), nullable=False)
    fCollisionSpinDamping = Column(Float(24), nullable=False)
    fCollisionThreshold = Column(Float(24), nullable=False)
    fTorqueRollFactor = Column(Float(24), nullable=False)
    fTorquePitchFactor = Column(Float(24), nullable=False)
    fTorqueYawFactor = Column(Float(24), nullable=False)
    fInertiaRoll = Column(Float(24), nullable=False)
    fInertiaPitch = Column(Float(24), nullable=False)
    fInertiaYaw = Column(Float(24), nullable=False)
    fExtraTorqueFactor = Column(Float(24), nullable=False)
    fCenterOfMassFwd = Column(Float(24), nullable=False)
    fCenterOfMassUp = Column(Float(24), nullable=False)
    fCenterOfMassRight = Column(Float(24), nullable=False)
    fWheelHardpointFrontFwd = Column(Float(24), nullable=False)
    fWheelHardpointFrontUp = Column(Float(24), nullable=False)
    fWheelHardpointFrontRight = Column(Float(24), nullable=False)
    fWheelHardpointRearFwd = Column(Float(24), nullable=False)
    fWheelHardpointRearUp = Column(Float(24), nullable=False)
    fWheelHardpointRearRight = Column(Float(24), nullable=False)
    fInputTurnSpeed = Column(Float(24), nullable=False)
    fInputDeadTurnBackSpeed = Column(Float(24), nullable=False)
    fInputAccelSpeed = Column(Float(24), nullable=False)
    fInputDeadAccelDownSpeed = Column(Float(24), nullable=False)
    fInputDecelSpeed = Column(Float(24), nullable=False)
    fInputDeadDecelDownSpeed = Column(Float(24), nullable=False)
    fInputSlopeChangePointX = Column(Float(24), nullable=False)
    fInputInitialSlope = Column(Float(24), nullable=False)
    fInputDeadZone = Column(Float(24), nullable=False)
    fAeroAirDensity = Column(Float(24), nullable=False)
    fAeroFrontalArea = Column(Float(24), nullable=False)
    fAeroDragCoefficient = Column(Float(24), nullable=False)
    fAeroLiftCoefficient = Column(Float(24), nullable=False)
    fAeroExtraGravity = Column(Float(24), nullable=False)
    fBoostTopSpeed = Column(Float(24), nullable=False)
    fBoostAccelerateChange = Column(Float(24), nullable=False)
    fBoostDampingChange = Column(Float(24), nullable=False)
    fPowerslideNeutralAngle = Column(Float(24), nullable=False)
    fPowerslideTorqueStrength = Column(Float(24), nullable=False)
    iPowerslideNumTorqueApplications = Column(Integer, nullable=False)
    fSkillCost = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioSpeedThresholdLightHit = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioTimeoutLightHit = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioSpeedThresholdHeavyHit = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioTimeoutHeavyHit = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioAirtimeForLightLand = Column(Float(24), nullable=False, server_default=text('((0))'))
    AudioAirtimeForHeavyLand = Column(Float(24), nullable=False, server_default=text('((0))'))
    name = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'))
    hkxFilename = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    fBoostCostPerSecond = Column(Float(24))
    fImaginationTankSize = Column(Float(24))
    fWreckSpeedBase = Column(Float(24))
    fWreckSpeedPercent = Column(Float(24))
    fWreckMinAngle = Column(Float(24))
    AudioEventEngine = Column(Unicode(128))
    AudioEventSkid = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventLightHit = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventHeavyHit = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventStart = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadConcrete = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadSand = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadWood = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadDirt = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadPlastic = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadGrass = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadGravel = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadMud = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadWater = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadSnow = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadIce = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadMetal = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventTreadLeaves = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventLightLand = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    AudioEventHeavyLand = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))


class VehicleStatMap(Base):
    __tablename__ = 'VehicleStatMap'

    id = Column(Integer, primary_key=True, nullable=False)
    ModuleStat = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False)
    HavokStat = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False)
    HavokChangePerModuleStat = Column(Float(24), nullable=False)


class WhatsCoolItemSpotlight(Base):
    __tablename__ = 'WhatsCoolItemSpotlight'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    itemID = Column(Integer, nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    description = Column(Unicode(512))
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class WhatsCoolNewsAndTips(Base):
    __tablename__ = 'WhatsCoolNewsAndTips'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    type = Column(Integer, nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    text_ = Column('text', Unicode(512))
    iconID = Column(Integer)
    storyTitle = Column(Unicode(512))
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class WorldConfig(Base):
    __tablename__ = 'WorldConfig'

    WorldConfigID = Column(Integer, primary_key=True)
    pegravityvalue = Column(Float(24))
    pebroadphaseworldsize = Column(Float(24))
    pegameobjscalefactor = Column(Float(24))
    character_rotation_speed = Column(Float(24))
    character_walk_forward_speed = Column(Float(24))
    character_walk_backward_speed = Column(Float(24))
    character_walk_strafe_speed = Column(Float(24))
    character_walk_strafe_forward_speed = Column(Float(24))
    character_walk_strafe_backward_speed = Column(Float(24))
    character_run_backward_speed = Column(Float(24))
    character_run_strafe_speed = Column(Float(24))
    character_run_strafe_forward_speed = Column(Float(24))
    character_run_strafe_backward_speed = Column(Float(24))
    global_cooldown = Column(Float(24))
    characterGroundedTime = Column(Float(24))
    characterGroundedSpeed = Column(Float(24))
    globalImmunityTime = Column(Float(24))
    character_max_slope = Column(Float(24))
    defaultrespawntime = Column(Float(24))
    mission_tooltip_timeout = Column(Float(24))
    vendor_buy_multiplier = Column(Float(24))
    pet_follow_radius = Column(Float(24))
    character_eye_height = Column(Float(24))
    flight_vertical_velocity = Column(Float(24))
    flight_airspeed = Column(Float(24))
    flight_fuel_ratio = Column(Float(24))
    flight_max_airspeed = Column(Float(24))
    fReputationPerVote = Column(Float(24))
    nPropertyCloneLimit = Column(Integer)
    defaultHomespaceTemplate = Column(Integer)
    coins_lost_on_death_percent = Column(Float(24))
    coins_lost_on_death_min = Column(Integer)
    coins_lost_on_death_max = Column(Integer)
    character_votes_per_day = Column(Integer)
    property_moderation_request_approval_cost = Column(Integer)
    property_moderation_request_review_cost = Column(Integer)
    propertyModRequestsAllowedSpike = Column(Integer)
    propertyModRequestsAllowedInterval = Column(Integer)
    propertyModRequestsAllowedTotal = Column(Integer)
    propertyModRequestsSpikeDuration = Column(Integer)
    propertyModRequestsIntervalDuration = Column(Integer)
    modelModerateOnCreate = Column(Boolean, server_default=text('((0))'))
    defaultPropertyMaxHeight = Column(Float(24))
    reputationPerVoteCast = Column(Float(24))
    reputationPerVoteReceived = Column(Float(24))
    showcaseTopModelConsiderationBattles = Column(Integer)
    reputationPerBattlePromotion = Column(Float(24))
    coins_lost_on_death_min_timeout = Column(Float(24))
    coins_lost_on_death_max_timeout = Column(Float(24))
    mail_base_fee = Column(Integer)
    mail_percent_attachment_fee = Column(Float(24))
    propertyReputationDelay = Column(Integer)


class ZoneLoadingTips(Base):
    __tablename__ = 'ZoneLoadingTips'

    id = Column(Integer, primary_key=True)
    localize = Column(Boolean, nullable=False)
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    weight = Column(TINYINT, nullable=False, server_default=text('((1))'))
    zoneid = Column(Integer)
    tip1 = Column(Unicode(1024))
    tip2 = Column(Unicode(1024))
    title = Column(Unicode(1024))
    imagelocation = Column(Unicode(256))
    gate_version = Column(Unicode(32))
    targetVersion = Column(Unicode(32))


class ZoneSummary(Base):
    __tablename__ = 'ZoneSummary'

    zoneID = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    _uniqueID = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    value = Column(Integer)


class ZoneTable(Base):
    __tablename__ = 'ZoneTable'

    zoneID = Column(Integer, primary_key=True)
    petsAllowed = Column(Boolean, nullable=False)
    PlayerLoseCoinsOnDeath = Column(Boolean, nullable=False, server_default=text('((1))'))
    disableSaveLoc = Column(Boolean, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    zoneName = Column(Unicode(256))
    scriptID = Column(Integer, server_default=text('((-1))'))
    ghostdistance_min = Column(Float(24))
    ghostdistance = Column(Float(24), server_default=text('((200.0))'))
    population_soft_cap = Column(Integer, server_default=text('((80))'))
    population_hard_cap = Column(Integer, server_default=text('((120))'))
    DisplayDescription = Column(Unicode(256))
    mapFolder = Column(Unicode(256))
    smashableMinDistance = Column(Float(24))
    smashableMaxDistance = Column(Float(24))
    mixerProgram = Column(Unicode(128))
    clientPhysicsFramerate = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    serverPhysicsFramerate = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    zoneControlTemplate = Column(Integer)
    widthInChunks = Column(SmallInteger)
    heightInChunks = Column(SmallInteger)
    localize = Column(Boolean, server_default=text('((1))'))
    fZoneWeight = Column(Float(53))
    summary = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    thumbnail = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    teamRadius = Column(Float(24))
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class BrickAttributes(Base):
    __tablename__ = 'brickAttributes'

    ID = Column(TINYINT, primary_key=True)
    display_order = Column(TINYINT, nullable=False, server_default=text('((0))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    name = Column(String(40, 'SQL_Latin1_General_CP1_CI_AS'))
    icon_asset = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class Dtproperties(Base):
    __tablename__ = 'dtproperties'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True, nullable=False)
    property = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'), primary_key=True, nullable=False)
    version = Column(Integer, nullable=False, server_default=text('((0))'))
    objectid = Column(Integer)
    value = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    uvalue = Column(Unicode(255))
    lvalue = Column(BLOB)


class MapAnimationFlags(Base):
    __tablename__ = 'mapAnimationFlags'

    ID = Column(TINYINT, Identity(start=1, increment=1), primary_key=True)
    FlagName = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    Description = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))


class MapAnimationPriorities(Base):
    __tablename__ = 'mapAnimationPriorities'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    name = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'))
    priority = Column(Float(24))


class MapAssetType(Base):
    __tablename__ = 'mapAssetType'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    label = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))
    pathdir = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'))
    typelabel = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class MapComponentType(Base):
    __tablename__ = 'mapComponentType'

    id = Column(Integer, primary_key=True)
    label = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))
    table = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))


class MapIcon(Base):
    __tablename__ = 'mapIcon'

    LOT = Column(Integer, primary_key=True, nullable=False)
    iconID = Column(Integer, nullable=False)
    iconState = Column(Integer, primary_key=True, nullable=False)


class MapItemTypes(Base):
    __tablename__ = 'mapItemTypes'

    id = Column(Integer, primary_key=True)
    description = Column(Unicode(50), nullable=False)
    equipLocation = Column(Unicode(50))


class MapRenderEffects(Base):
    __tablename__ = 'mapRenderEffects'

    id = Column(Integer, primary_key=True)
    gameID = Column(Integer, nullable=False)
    description = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))


class MapShaders(Base):
    __tablename__ = 'mapShaders'

    id = Column(Integer, primary_key=True)
    label = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    gameValue = Column(Integer)
    priority = Column(Integer)


class MapTextureResource(Base):
    __tablename__ = 'mapTextureResource'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    SurfaceType = Column(Integer, nullable=False, server_default=text('((0))'))
    texturepath = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))
    soundtype = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))


class MapBlueprintCategory(Base):
    __tablename__ = 'map_BlueprintCategory'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    enabled = Column(Boolean, nullable=False)
    description = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))

    Blueprints = relationship('Blueprints', back_populates='map_BlueprintCategory')


class TestCharacters(Base):
    __tablename__ = 'testCharacters'

    id = Column(BigInteger, primary_key=True)
    propertycloneid = Column(Integer, Identity(start=1, increment=1), nullable=False)
    name = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    objid = Column(Integer)
    timestamp = Column(DateTime)
    online = Column(Boolean)
    pendingname = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    requiresrename = Column(Boolean)


class Testtable2(Base):
    __tablename__ = 'testtable2'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    realVal = Column(Float(24))
    varCharVal = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    intVal = Column(Integer)
    int64val = Column(BigInteger)
    bitVal = Column(Boolean)
    smallVal = Column(SmallInteger)
    tinyVal = Column(TINYINT)
    doubleVal = Column(Float(53))
    binaryVal = Column(LargeBinary)
    timeVal = Column(DateTime)
    charVal = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    name = Column(Unicode(50))
    nameLONG = Column(Unicode)
    nameShort = Column(NCHAR(4))
    xmlData = Column(TEXT)


t_vBrickRenderAssets = Table(
    'vBrickRenderAssets', metadata,
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('type', Unicode(64), nullable=False),
    Column('description', String(512, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('displayName', Unicode(256)),
    Column('NDObjectID', Integer, nullable=False),
    Column('LEGOBrickID', Integer, nullable=False),
    Column('render_component', Integer, nullable=False),
    Column('render_asset', String(256, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_vComponentsRegistryWithTypes = Table(
    'vComponentsRegistryWithTypes', metadata,
    Column('id', Integer, nullable=False),
    Column('component_type', Integer, nullable=False),
    Column('component_id', Integer, nullable=False),
    Column('label', String(32, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('table', String(32, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_vObjectComponentAssets = Table(
    'vObjectComponentAssets', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('description', String(512, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('displayName', Unicode(256)),
    Column('component_type', Integer, nullable=False),
    Column('component_id', Integer, nullable=False),
    Column('asset', String(256, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_vRewardModelFileNames = Table(
    'vRewardModelFileNames', metadata,
    Column('LOT', Integer, nullable=False),
    Column('displayName', Unicode(256)),
    Column('lxfmlFileName', String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
)


t_vwBrickPrice = Table(
    'vwBrickPrice', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('LEGOBrickID', Integer, nullable=False),
    Column('baseValue', Integer)
)


t_vwDestructibleComponent = Table(
    'vwDestructibleComponent', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('type', Unicode(64), nullable=False),
    Column('component_type', Integer, nullable=False),
    Column('faction', Integer),
    Column('life', Integer),
    Column('LootMatrixIndex', Integer),
    Column('CurrencyIndex', Integer),
    Column('level', Integer),
    Column('isnpc', Boolean),
    Column('nametag', Boolean),
    Column('localize', Boolean, nullable=False)
)


t_vwDestructibleComponentNPCs = Table(
    'vwDestructibleComponentNPCs', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('type', Unicode(64), nullable=False),
    Column('component_type', Integer, nullable=False),
    Column('faction', Integer),
    Column('life', Integer),
    Column('LootMatrixIndex', Integer),
    Column('CurrencyIndex', Integer),
    Column('level', Integer),
    Column('isnpc', Boolean)
)


t_vwDestructibleComponentNPCsTAGS = Table(
    'vwDestructibleComponentNPCsTAGS', metadata,
    Column('id', Integer, nullable=False),
    Column('name', String(256, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('type', Unicode(64), nullable=False),
    Column('component_type', Integer, nullable=False),
    Column('faction', Integer),
    Column('life', Integer),
    Column('LootMatrixIndex', Integer),
    Column('CurrencyIndex', Integer),
    Column('level', Integer),
    Column('isnpc', Boolean)
)


class AICombatRoles(Base):
    __tablename__ = 'AICombatRoles'

    id = Column(Integer, Identity(start=0, increment=1), primary_key=True)
    preferredRole = Column(ForeignKey('AICombatRoleTypes.id'))
    description = Column(Unicode(50))
    specifiedMinRangeNOUSE = Column(Float(53), server_default=text('((-1))'))
    specifiedMaxRangeNOUSE = Column(Float(53), server_default=text('((-1))'))
    specificMinRange = Column(Float(24))
    specificMaxRange = Column(Float(24))

    AICombatRoleTypes = relationship('AICombatRoleTypes', back_populates='AICombatRoles')


class ActivityText(Base):
    __tablename__ = 'ActivityText'

    activityID = Column(ForeignKey('Activities.ActivityID'), primary_key=True, nullable=False, index=True)
    type = Column(Unicode(50), primary_key=True, nullable=False)
    text_ = Column('text', Unicode(256), primary_key=True, nullable=False)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    subjectText = Column(Unicode(256))
    gate_version = Column(Unicode(32))

    Activities = relationship('Activities', back_populates='ActivityText')


class Animations(Base):
    __tablename__ = 'Animations'

    animationGroupID = Column(ForeignKey('AnimationIndex.animationGroupID'), primary_key=True, nullable=False)
    animation_type = Column(Unicode(32), primary_key=True, nullable=False)
    animation_name = Column(Unicode(64), primary_key=True, nullable=False)
    chance_to_play = Column(Float(24), nullable=False)
    min_loops = Column(Integer, nullable=False)
    max_loops = Column(Integer, nullable=False)
    animation_length = Column(Float(24), nullable=False)
    hideEquip = Column(Boolean, nullable=False, server_default=text('((0))'))
    ignoreUpperBody = Column(Boolean, nullable=False, server_default=text('((0))'))
    restartable = Column(Boolean, nullable=False, server_default=text('((0))'))
    sound1 = Column(Unicode(128))
    sound2 = Column(Unicode(128))
    sound3 = Column(Unicode(128))
    sound4 = Column(Unicode(128))
    sound5 = Column(Unicode(128))
    leftSound = Column(Unicode(128))
    rightSound = Column(Unicode(128))
    face_animation_name = Column(Unicode(128))
    priority = Column(Float(24))
    blendTime = Column(Float(24))

    AnimationIndex = relationship('AnimationIndex', back_populates='Animations')


class BehaviorEffect(Base):
    __tablename__ = 'BehaviorEffect'

    effectID = Column(Integer, primary_key=True, nullable=False)
    effectType = Column(Unicode(259), primary_key=True, nullable=False)
    attachToObject = Column(Boolean, nullable=False, server_default=text('((0))'))
    useSecondary = Column(Boolean, nullable=False, server_default=text('((0))'))
    soundIs3D = Column(Boolean, nullable=False, server_default=text('((1))'))
    effectName = Column(Unicode(259))
    trailID = Column(ForeignKey('TrailEffects.trailID'))
    pcreateDuration = Column(Float(24))
    soundName = Column(Unicode(259))
    animationName = Column(Unicode(250))
    boneName = Column(Unicode(500))
    cameraEffectType = Column(Integer)
    cameraDuration = Column(Float(24))
    cameraFrequency = Column(Float(24))
    cameraXAmp = Column(Float(24))
    cameraYAmp = Column(Float(24))
    cameraZAmp = Column(Float(24))
    cameraRotFrequency = Column(Float(24))
    cameraRoll = Column(Float(24))
    cameraPitch = Column(Float(24))
    cameraYaw = Column(Float(24))
    AudioEventGUID = Column(Unicode(128))
    renderEffectType = Column(Integer)
    renderEffectTime = Column(Float(24))
    renderStartVal = Column(Float(24))
    renderEndVal = Column(Float(24))
    renderDelayVal = Column(Float(24))
    renderValue1 = Column(Float(24))
    renderValue2 = Column(Float(24))
    renderValue3 = Column(Float(24))
    renderRGBA = Column(NCHAR(16))
    renderShaderVal = Column(Integer)
    motionID = Column(ForeignKey('MotionFX.id'))
    meshID = Column(Integer)
    meshDuration = Column(Float(24))
    meshLockedNode = Column(Unicode(128))

    MotionFX = relationship('MotionFX', back_populates='BehaviorEffect')
    TrailEffects = relationship('TrailEffects', back_populates='BehaviorEffect')


class BehaviorTemplate(Base):
    __tablename__ = 'BehaviorTemplate'

    behaviorID = Column(Integer, primary_key=True)
    templateID = Column(ForeignKey('BehaviorTemplateName.templateID'), nullable=False)
    effectID = Column(Integer, nullable=False, server_default=text('((0))'))
    effectHandle = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))

    BehaviorTemplateName = relationship('BehaviorTemplateName', back_populates='BehaviorTemplate')
    BehaviorParameter = relationship('BehaviorParameter', back_populates='BehaviorTemplate')
    SkillBehavior = relationship('SkillBehavior', back_populates='BehaviorTemplate')


class Blueprints(Base):
    __tablename__ = 'Blueprints'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(64, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    accountid = Column(BigInteger, nullable=False)
    characterid = Column(BigInteger, nullable=False)
    price = Column(Integer, nullable=False)
    categoryid = Column(ForeignKey('map_BlueprintCategory.id'), nullable=False)
    deleted = Column(Boolean, nullable=False)
    created = Column(DateTime, nullable=False)
    modified = Column(DateTime, nullable=False)
    description = Column(String(128, 'SQL_Latin1_General_CP1_CI_AS'))
    rating = Column(Integer)
    lxfpath = Column(String(256, 'SQL_Latin1_General_CP1_CI_AS'))

    map_BlueprintCategory = relationship('MapBlueprintCategory', back_populates='Blueprints')


class BrickIDTable(Base):
    __tablename__ = 'BrickIDTable'

    NDObjectID = Column(ForeignKey('Objects.id'), nullable=False)
    LEGOBrickID = Column(Integer, primary_key=True)

    Objects = relationship('Objects', back_populates='BrickIDTable')


class CurrencyDenominations(Base):
    __tablename__ = 'CurrencyDenominations'

    value = Column(Integer, primary_key=True)
    objectid = Column(ForeignKey('Objects.id'), nullable=False)

    Objects = relationship('Objects', back_populates='CurrencyDenominations')


class CurrencyTable(Base):
    __tablename__ = 'CurrencyTable'
    __table_args__ = (
        Index('IX_CurrencyTable', 'currencyIndex', 'npcminlevel', unique=True),
    )

    npcminlevel = Column(SmallInteger, nullable=False)
    minvalue = Column(Integer, nullable=False)
    maxvalue = Column(Integer, nullable=False)
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    currencyIndex = Column(ForeignKey('CurrencyIndex.CurrencyIndex'))

    CurrencyIndex = relationship('CurrencyIndex', back_populates='CurrencyTable')


class DestructibleComponent(Base):
    __tablename__ = 'DestructibleComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    death_behavior = Column(Integer, nullable=False, server_default=text('((0))'))
    attack_priority = Column(Integer, nullable=False, server_default=text('((1))'))
    faction = Column(Integer)
    factionList = Column(Unicode(32))
    life = Column(Integer)
    imagination = Column(Integer)
    LootMatrixIndex = Column(ForeignKey('LootMatrixIndex.LootMatrixIndex'))
    CurrencyIndex = Column(ForeignKey('CurrencyIndex.CurrencyIndex'))
    level = Column(Integer)
    armor = Column(Float(24))
    protection_disruption = Column(Float(24))
    protection_elemental = Column(Float(24))
    protection_physical = Column(Float(24))
    isnpc = Column(Boolean, server_default=text('((0))'))
    isSmashable = Column(Boolean, server_default=text('((0))'))

    CurrencyIndex_ = relationship('CurrencyIndex', back_populates='DestructibleComponent')
    LootMatrixIndex_ = relationship('LootMatrixIndex', back_populates='DestructibleComponent')


class ItemComponent(Base):
    __tablename__ = 'ItemComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    isKitPiece = Column(Boolean, nullable=False)
    itemType = Column(Integer, nullable=False, server_default=text('((-1))'))
    inLootTable = Column(Boolean, nullable=False)
    inVendor = Column(Boolean, nullable=False)
    isUnique = Column(Boolean, nullable=False)
    isBOP = Column(Boolean, nullable=False)
    isBOE = Column(Boolean, nullable=False)
    readyForQA = Column(Boolean, nullable=False)
    isTwoHanded = Column(Boolean, nullable=False)
    equipLocation = Column(Unicode(64), server_default=text('((0))'))
    baseValue = Column(Integer)
    rarity = Column(Integer)
    itemInfo = Column(BigInteger)
    reqFlagID = Column(Integer, server_default=text('((0))'))
    reqSpecialtyID = Column(Integer, server_default=text('((0))'))
    reqSpecRank = Column(Integer, server_default=text('((0))'))
    reqAchievementID = Column(Integer, server_default=text('((0))'))
    stackSize = Column(Integer, server_default=text('((0))'))
    color1 = Column(Integer)
    decal = Column(Integer)
    offsetGroupID = Column(ForeignKey('AccessoryDefaultLoc.GroupID'))
    buildTypes = Column(Integer, server_default=text('((0))'))
    reqPrecondition = Column(Unicode(50))
    animationFlag = Column(Integer)
    equipEffects = Column(Integer)
    itemRating = Column(Integer)
    minNumRequired = Column(TINYINT)
    delResIndex = Column(Integer)
    currencyLOT = Column(Integer)
    altCurrencyCost = Column(Integer)
    subItems = Column(NCHAR(50))
    audioEventUse = Column(Unicode(50))

    AccessoryDefaultLoc = relationship('AccessoryDefaultLoc', back_populates='ItemComponent')


class LootMatrix(Base):
    __tablename__ = 'LootMatrix'
    __table_args__ = (
        Index('IX_LootMatrix', 'LootMatrixIndex', 'LootTableIndex', unique=True),
    )

    LootMatrixIndex = Column(ForeignKey('LootMatrixIndex.LootMatrixIndex'), nullable=False)
    LootTableIndex = Column(ForeignKey('LootTableIndex.LootTableIndex'), nullable=False)
    RarityTableIndex = Column(ForeignKey('RarityTableIndex.RarityTableIndex'), nullable=False)
    percent = Column(Float(24), nullable=False)
    minToDrop = Column(Integer, nullable=False, server_default=text('((0))'))
    maxToDrop = Column(Integer, nullable=False, server_default=text('((1))'))
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    flagID = Column(Integer)
    gate_version = Column(String(32, 'SQL_Latin1_General_CP1_CI_AS'))

    LootMatrixIndex_ = relationship('LootMatrixIndex', back_populates='LootMatrix')
    LootTableIndex_ = relationship('LootTableIndex', back_populates='LootMatrix')
    RarityTableIndex_ = relationship('RarityTableIndex', back_populates='LootMatrix')


class LootTable(Base):
    __tablename__ = 'LootTable'
    __table_args__ = (
        Index('IX_LootTable', 'LootTableIndex', 'itemid', unique=True),
    )

    itemid = Column(Integer, nullable=False)
    LootTableIndex = Column(ForeignKey('LootTableIndex.LootTableIndex'), nullable=False)
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    sortPriority = Column(Integer, nullable=False, server_default=text('((0))'))
    MissionDrop = Column(Boolean, server_default=text('((0))'))

    LootTableIndex_ = relationship('LootTableIndex', back_populates='LootTable')


class MissionTasks(Base):
    __tablename__ = 'MissionTasks'

    id = Column(ForeignKey('Missions.id'), nullable=False, index=True)
    taskType = Column(Integer, nullable=False)
    uid = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    target = Column(Integer)
    targetGroup = Column(Unicode)
    targetValue = Column(Integer)
    taskParam1 = Column(Unicode(1024))
    description = Column(Unicode(1024))
    largeTaskIcon = Column(Unicode(256))
    IconID = Column(Integer)
    largeTaskIconID = Column(Integer)
    gate_version = Column(Unicode(32))

    Missions = relationship('Missions', back_populates='MissionTasks')


class MissionText(Missions):
    __tablename__ = 'MissionText'

    id = Column(ForeignKey('Missions.id'), primary_key=True)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    description = Column(Unicode(1024))
    offer = Column(Unicode(1024))
    in_progress = Column(Unicode(1024))
    ready_to_complete = Column(Unicode(1024))
    story_icon = Column(Unicode(128))
    completion_fail_tip = Column(Unicode(1024))
    completion_succeed_tip = Column(Unicode(1024))
    chat_state_1 = Column(Unicode(256))
    chat_state_2 = Column(Unicode(256))
    chat_state_3 = Column(Unicode(256))
    chat_state_4 = Column(Unicode(256))
    missionIcon = Column(Unicode(256))
    offerNPCIcon = Column(Unicode(256))
    IconID = Column(Integer)
    accept_chat_bubble = Column(Unicode(1024))
    offer_repeatable = Column(Unicode(1024))
    bubble_prereq_not_met = Column(Unicode(1024))
    chat_state_3_turnin = Column(Unicode(1024))
    chat_state_4_turnin = Column(Unicode(1024))
    state_1_anim = Column(Unicode(256))
    state_2_anim = Column(Unicode(256))
    state_3_anim = Column(Unicode(256))
    state_4_anim = Column(Unicode(256))
    state_3_turnin_anim = Column(Unicode(256))
    state_4_turnin_anim = Column(Unicode(256))
    onclick_anim = Column(Unicode(256))
    CinematicAccepted = Column(Unicode(256))
    CinematicAcceptedLeadin = Column(Float(24))
    CinematicCompleted = Column(Unicode(256))
    CinematicCompletedLeadin = Column(Float(24))
    CinematicRepeatable = Column(Unicode(256))
    CinematicRepeatableLeadin = Column(Float(24))
    CinematicRepeatableCompleted = Column(Unicode(256))
    CinematicRepeatableCompletedLeadin = Column(Float(24))
    AudioEventGUID_Interact = Column(Unicode(256))
    AudioEventGUID_OfferAccept = Column(Unicode(256))
    AudioEventGUID_OfferDeny = Column(Unicode(256))
    AudioEventGUID_Completed = Column(Unicode(256))
    AudioEventGUID_TurnIn = Column(Unicode(256))
    AudioEventGUID_Failed = Column(Unicode(256))
    AudioEventGUID_Progress = Column(Unicode(256))
    AudioMusicCue_OfferAccept = Column(Unicode(256))
    AudioMusicCue_TurnIn = Column(Unicode(256))
    turnInIconID = Column(Integer)
    gate_version = Column(Unicode(32))


class RarityTable(Base):
    __tablename__ = 'RarityTable'
    __table_args__ = (
        Index('IX_RarityTable', 'RarityTableIndex', 'randmax', unique=True),
    )

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    randmax = Column(Float(24), nullable=False)
    rarity = Column(Integer, nullable=False)
    RarityTableIndex = Column(ForeignKey('RarityTableIndex.RarityTableIndex'), nullable=False)

    RarityTableIndex_ = relationship('RarityTableIndex', back_populates='RarityTable')


class SpeedchatMenu(Base):
    __tablename__ = 'SpeedchatMenu'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    parentId = Column(Integer)
    emoteId = Column(ForeignKey('Emotes.id'))
    menuText = Column(Unicode(35))
    imageName = Column(Unicode(256))
    gate_version = Column(Unicode(32))

    Emotes = relationship('Emotes', back_populates='SpeedchatMenu')


class TextLanguage(TextDescription):
    __tablename__ = 'TextLanguage'

    TextID = Column(ForeignKey('TextDescription.TextID'), primary_key=True)
    LanguageID = Column(ForeignKey('LanguageType.LanguageID'), nullable=False)
    Text = Column(Unicode(1024), nullable=False)

    LanguageType = relationship('LanguageType', back_populates='TextLanguage')


class VendorComponent(Base):
    __tablename__ = 'VendorComponent'

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    buyScalar = Column(Float(24), nullable=False, server_default=text('((1))'))
    sellScalar = Column(Float(24), nullable=False, server_default=text('((1))'))
    refreshTimeSeconds = Column(Float(24), nullable=False, server_default=text('((1800))'))
    LootMatrixIndex = Column(ForeignKey('LootMatrixIndex.LootMatrixIndex'), nullable=False)

    LootMatrixIndex_ = relationship('LootMatrixIndex', back_populates='VendorComponent')


class BehaviorParameter(Base):
    __tablename__ = 'BehaviorParameter'

    behaviorID = Column(ForeignKey('BehaviorTemplate.behaviorID'), primary_key=True, nullable=False)
    parameterID = Column(Unicode(32), primary_key=True, nullable=False)
    value = Column(Float(24))

    BehaviorTemplate = relationship('BehaviorTemplate', back_populates='BehaviorParameter')


class SkillBehavior(Base):
    __tablename__ = 'SkillBehavior'

    skillID = Column(Integer, primary_key=True)
    behaviorID = Column(ForeignKey('BehaviorTemplate.behaviorID'), nullable=False)
    name = Column(Unicode(128), nullable=False)
    description = Column(Unicode(1024), nullable=False)
    imaginationcost = Column(Integer, nullable=False, server_default=text('((0))'))
    cooldown = Column(Float(24), nullable=False)
    inNpcEditor = Column(Boolean, nullable=False, server_default=text('((0))'))
    hideIcon = Column(Boolean, nullable=False, server_default=text('((0))'))
    localize = Column(Boolean, nullable=False, server_default=text('((1))'))
    locStatus = Column(SmallInteger, nullable=False, server_default=text('((0))'))
    cooldowngroup = Column(Integer)
    skillIcon = Column(Integer)
    oomSkillID = Column(Unicode(500))
    oomBehaviorEffectID = Column(Integer)
    castTypeDesc = Column(Integer)
    imBonusUI = Column(Integer)
    lifeBonusUI = Column(Integer)
    armorBonusUI = Column(Integer)
    damageUI = Column(Integer)
    descriptionUI = Column(Unicode(1024))
    gate_version = Column(Unicode(32))

    BehaviorTemplate = relationship('BehaviorTemplate', back_populates='SkillBehavior')
    ObjectSkills = relationship('ObjectSkills', back_populates='SkillBehavior')


class ObjectSkills(Base):
    __tablename__ = 'ObjectSkills'

    objectTemplate = Column(ForeignKey('Objects.id'), primary_key=True, nullable=False)
    skillID = Column(ForeignKey('SkillBehavior.skillID'), primary_key=True, nullable=False)
    castOnType = Column(Integer)
    AICombatWeight = Column(Integer)

    Objects = relationship('Objects', back_populates='ObjectSkills')
    SkillBehavior = relationship('SkillBehavior', back_populates='ObjectSkills')
