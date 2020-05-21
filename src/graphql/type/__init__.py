"""GraphQL Type System

The :mod:`graphql.type` package is responsible for defining GraphQL types and schema.
"""

from ..pyutils import Path as ResponsePath

from .schema import (
    # Predicate
    is_schema,
    # Assertion
    assert_schema,
    # GraphQL Schema definition
    GraphQLSchema,
)

from .definition import (
    # Predicates
    is_type,
    is_scalar_type,
    is_object_type,
    is_interface_type,
    is_union_type,
    is_enum_type,
    is_input_object_type,
    is_list_type,
    is_non_null_type,
    is_input_type,
    is_output_type,
    is_leaf_type,
    is_composite_type,
    is_abstract_type,
    is_wrapping_type,
    is_nullable_type,
    is_named_type,
    is_required_argument,
    is_required_input_field,
    # Assertions
    assert_type,
    assert_scalar_type,
    assert_object_type,
    assert_interface_type,
    assert_union_type,
    assert_enum_type,
    assert_input_object_type,
    assert_list_type,
    assert_non_null_type,
    assert_input_type,
    assert_output_type,
    assert_leaf_type,
    assert_composite_type,
    assert_abstract_type,
    assert_wrapping_type,
    assert_nullable_type,
    assert_named_type,
    # Un-modifiers
    get_nullable_type,
    get_named_type,
    # Definitions
    GraphQLScalarType,
    GraphQLObjectType,
    GraphQLInterfaceType,
    GraphQLUnionType,
    GraphQLEnumType,
    GraphQLInputObjectType,
    # Type Wrappers
    GraphQLList,
    GraphQLNonNull,
    # Types
    GraphQLType,
    GraphQLInputType,
    GraphQLOutputType,
    GraphQLLeafType,
    GraphQLCompositeType,
    GraphQLAbstractType,
    GraphQLWrappingType,
    GraphQLNullableType,
    GraphQLNamedType,
    Thunk,
    GraphQLArgument,
    GraphQLArgumentMap,
    GraphQLEnumValue,
    GraphQLEnumValueMap,
    GraphQLField,
    GraphQLFieldMap,
    GraphQLInputField,
    GraphQLInputFieldMap,
    GraphQLScalarSerializer,
    GraphQLScalarValueParser,
    GraphQLScalarLiteralParser,
    # Resolvers
    GraphQLFieldResolver,
    GraphQLTypeResolver,
    GraphQLIsTypeOfFn,
    GraphQLResolveInfo,
)

from .directives import (
    # Predicate
    is_directive,
    # Assertion
    assert_directive,
    # Directives Definition
    GraphQLDirective,
    # Built-in Directives defined by the Spec
    is_specified_directive,
    specified_directives,
    GraphQLIncludeDirective,
    GraphQLSkipDirective,
    GraphQLDeprecatedDirective,
    GraphQLSpecifiedByDirective,
    # Constant Deprecation Reason
    DEFAULT_DEPRECATION_REASON,
)

# Common built-in scalar instances.
from .scalars import (
    # Predicate
    is_specified_scalar_type,
    # Standard GraphQL Scalars
    specified_scalar_types,
    GraphQLInt,
    GraphQLFloat,
    GraphQLString,
    GraphQLBoolean,
    GraphQLID,
)

from .introspection import (
    # Predicate
    is_introspection_type,
    # GraphQL Types for introspection.
    introspection_types,
    # "Enum" of Type Kinds
    TypeKind,
    # Meta-field definitions.
    SchemaMetaFieldDef,
    TypeMetaFieldDef,
    TypeNameMetaFieldDef,
)

# Validate GraphQL schema.
from .validate import validate_schema, assert_valid_schema

__all__ = [
    "is_schema",
    "assert_schema",
    "GraphQLSchema",
    "is_type",
    "is_scalar_type",
    "is_object_type",
    "is_interface_type",
    "is_union_type",
    "is_enum_type",
    "is_input_object_type",
    "is_list_type",
    "is_non_null_type",
    "is_input_type",
    "is_output_type",
    "is_leaf_type",
    "is_composite_type",
    "is_abstract_type",
    "is_wrapping_type",
    "is_nullable_type",
    "is_named_type",
    "is_required_argument",
    "is_required_input_field",
    "assert_type",
    "assert_scalar_type",
    "assert_object_type",
    "assert_interface_type",
    "assert_union_type",
    "assert_enum_type",
    "assert_input_object_type",
    "assert_list_type",
    "assert_non_null_type",
    "assert_input_type",
    "assert_output_type",
    "assert_leaf_type",
    "assert_composite_type",
    "assert_abstract_type",
    "assert_wrapping_type",
    "assert_nullable_type",
    "assert_named_type",
    "get_nullable_type",
    "get_named_type",
    "GraphQLScalarType",
    "GraphQLObjectType",
    "GraphQLInterfaceType",
    "GraphQLUnionType",
    "GraphQLEnumType",
    "GraphQLInputObjectType",
    "GraphQLInputType",
    "GraphQLArgument",
    "GraphQLList",
    "GraphQLNonNull",
    "GraphQLType",
    "GraphQLInputType",
    "GraphQLOutputType",
    "GraphQLLeafType",
    "GraphQLCompositeType",
    "GraphQLAbstractType",
    "GraphQLWrappingType",
    "GraphQLNullableType",
    "GraphQLNamedType",
    "Thunk",
    "GraphQLArgument",
    "GraphQLArgumentMap",
    "GraphQLEnumValue",
    "GraphQLEnumValueMap",
    "GraphQLField",
    "GraphQLFieldMap",
    "GraphQLInputField",
    "GraphQLInputFieldMap",
    "GraphQLScalarSerializer",
    "GraphQLScalarValueParser",
    "GraphQLScalarLiteralParser",
    "GraphQLFieldResolver",
    "GraphQLTypeResolver",
    "GraphQLIsTypeOfFn",
    "GraphQLResolveInfo",
    "ResponsePath",
    "is_directive",
    "assert_directive",
    "is_specified_directive",
    "specified_directives",
    "GraphQLDirective",
    "GraphQLIncludeDirective",
    "GraphQLSkipDirective",
    "GraphQLDeprecatedDirective",
    "GraphQLSpecifiedByDirective",
    "DEFAULT_DEPRECATION_REASON",
    "is_specified_scalar_type",
    "specified_scalar_types",
    "GraphQLInt",
    "GraphQLFloat",
    "GraphQLString",
    "GraphQLBoolean",
    "GraphQLID",
    "is_introspection_type",
    "introspection_types",
    "TypeKind",
    "SchemaMetaFieldDef",
    "TypeMetaFieldDef",
    "TypeNameMetaFieldDef",
    "validate_schema",
    "assert_valid_schema",
]
